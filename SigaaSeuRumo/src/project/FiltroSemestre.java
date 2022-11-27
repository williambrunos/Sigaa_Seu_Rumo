package project;

public class FiltroSemestre extends FiltroDecorador{

	public FiltroSemestre(Filtro filtro) {
		super(filtro);
	}


	public String informarFiltros() {
		 return super.informarFiltros() + ", Semestre";
	}
}

