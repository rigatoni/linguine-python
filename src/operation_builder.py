def get_operation_handler(operation):
	if operation in globals():
		constructor = globals()[operation]
		return constructor()
	else:
		raise RuntimeError("The requested operation does not exist.")