from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from cogcomp.curator import Curator
from cogcomp.base.ttypes import ServiceUnavailableException

from nltk.corpus import propbank

class TransportOpened():

    def __init__(self, trans):
        self.trans = trans

    def __enter__(self):
        if not self.trans.isOpen():
            self.trans.open()
        return self.trans

    def __exit__(self, exctype, excinst, exctb):
        if self.trans.isOpen():
            self.trans.close()


def getPredicates(head):
    span = head.span
    if span.attributes is not None and len(span.attributes) > 0:
        predicate = span.attributes.get("predicate")
        sense = span.attributes.get("sense")
        return predicate, sense

def displayParseView(view, text):
    trees = view.trees
    for tree in trees:
        stack = [tree.top]
        res = ""

        while len(stack) > 0:
            headIndex = stack.pop(-1)
            head = tree.nodes[headIndex]
            if head.children is not None and len(head.children) > 0:

                print(getPredicates(head))

                for childIndex in head.children:
                    stack.append(childIndex)
                    child = tree.nodes[childIndex]
                    relation = head.children[childIndex]
                    res += relation + "(" + text[head.span.start : head.span.ending] + ", "
                    res += text[child.span.start : child.span.ending] + ")\n"
        print("Verb SRL predicate-argument structure:")
        print(res)

def getPropbankInfo(wordWithSense):
    try:
        word = propbank.roleset(wordWithSense)
    except ValueError:
        return None
    return word.findall("roles/role")

def getSemanticRoles(view, text):

    semanticRoles = []

    trees = view.trees
    for tree in trees:
        stack = [tree.top]

        while len(stack) > 0:
            headIndex = stack.pop(-1)
            head = tree.nodes[headIndex]
            if head.children is not None and len(head.children) > 0:

                predicate, sense = getPredicates(head)
                roles = getPropbankInfo(predicate + "." + sense)
                if roles is not None:
                    relatedRoles = []

                    for childIndex in head.children:
                        stack.append(childIndex)
                        child = tree.nodes[childIndex]
                        relation = head.children[childIndex]

                        if relation == "AM-NEG":
                            relatedRoles.append("NEGATED")
                        else:
                            n = relation[1]
                            for role in roles:
                                if role.attrib['n'] == n:
                                    relatedRoles.append((role.attrib['descr'], text[child.span.start : child.span.ending]))

                    semanticRoles.append(relatedRoles)
    return semanticRoles


def getSRLFeatures(view, text):

    srls = []

    trees = view.trees
    for tree in trees:
        stack = [tree.top]

        while len(stack) > 0:
            headIndex = stack.pop(-1)
            head = tree.nodes[headIndex]
            if head.children is not None and len(head.children) > 0:

                predicate, sense = getPredicates(head)
                roles = getPropbankInfo(predicate + "." + sense)
                if roles is not None:
                    relatedRoles = []

                    negated = False
                    for childIndex in head.children:
                        relation = head.children[childIndex]
                        if relation == "AM-NEG":
                            negated = True

                    if negated:
                        predicate = "!" + predicate

                    for childIndex in head.children:
                        stack.append(childIndex)
                        child = tree.nodes[childIndex]
                        relation = head.children[childIndex]

                        n = relation[1]
                        if n == "M":
                            srls.append((relation, predicate, text[child.span.start : child.span.ending], child.span.start, child.span.ending, sense))
                        else:
                            for role in roles:
                                if role.attrib['n'] == n:
                                    srls.append((role.attrib['descr'], predicate, text[child.span.start : child.span.ending], child.span.start, child.span.ending, sense))
    return srls

def setup():
    # Make socket
    transport = TSocket.TSocket('nlp.rit.edu', 9010)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TFramedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Curator.Client(protocol)

    return transport, client

def main():
    transport, client = setup()
    forceUpdate = True
    with TransportOpened(transport) as t:

        avail = client.describeAnnotations()
        for key in avail:
            print(key + " provided by " + avail[key])

        text = "A squirrel is storing a lot of nuts to prepare for a seasonal change in the environment."

        try:
            client.provide("ner", text, forceUpdate)
            record = client.provide("srl", text, forceUpdate)
        except:
            print("Error. Bad text?")
            return

        labelViews = record.labelViews
        clusterViews = record.clusterViews
        parseViews = record.parseViews

        displayParseView(parseViews.get("srl"), text)

        print("------------------------------------------------")
        print(text)
        srl = getSRLFeatures(parseViews.get("srl"), text)
        for x in srl:
            print(x)
        print("------------------------------------------------")

if __name__ == "__main__":
    main()
