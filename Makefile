$(eval varstop=--stop)

nao_para_no_erro:
	$(eval varstop=)

.reset:
	reset

testes_estaveis: .reset
	behave --tags=-wip @sequence.featureset $(varstop)

todos_testes: .reset
	behave @sequence.featureset $(varstop)
