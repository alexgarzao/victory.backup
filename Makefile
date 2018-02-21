$(eval varstop=--stop)

nao_para_no_erro:
	$(eval varstop=)

.reset:
	reset

testes_estaveis: .reset
	behave --tags=-wip @sequence.featureset $(varstop)

todos_testes: .reset
	behave @sequence.featureset $(varstop)

testes_outro_projeto:
	behave --tags=-wip ./features @/home/alexgarzao/go/src/github.com/GrupoZapVivaReal/newbiz-ms-example1/tests/bdd_steps_library/sequence.featureset
