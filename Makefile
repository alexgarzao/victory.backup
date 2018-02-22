ifndef FEATURES_PATH
$(error FEATURES_PATH is not set. Usage "make FEATURES_PATH=<DIR_FEATURES_PATH> rule", where rule=(stable|all). Optional parameters: dont_stop_on_error)
endif

$(eval varstop=--stop)

dont_stop_on_error:
	$(eval varstop=)

.reset:
	reset

stable: .reset
	behave --tags=-wip -D features_path=$(FEATURES_PATH)/ ./features @$(FEATURES_PATH)/sequence.featureset $(varstop)

all: .reset
	behave -D features_path=$(FEATURES_PATH)/ ./features @$(FEATURES_PATH)/sequence.featureset $(varstop)

