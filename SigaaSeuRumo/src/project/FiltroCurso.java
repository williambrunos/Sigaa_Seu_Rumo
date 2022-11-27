package project;

public class FiltroCurso extends FiltroDecorador{

	public FiltroCurso(Filtro filtro) {
		super(filtro);
	}

	public String informarFiltros() {
		 return super.informarFiltros() + ", Curso";
	}
}


