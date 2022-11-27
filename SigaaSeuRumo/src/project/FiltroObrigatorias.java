package project;

public class FiltroObrigatorias extends FiltroDecorador {
	public FiltroObrigatorias(Filtro filtro) {
		super(filtro);
	}


	public String informarFiltros() {
		 return super.informarFiltros() + ", Obrigatorias";
	}
}
