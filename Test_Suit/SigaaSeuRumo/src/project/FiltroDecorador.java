package project;

public abstract class FiltroDecorador implements Filtro {
	private final Filtro filtroDecorador;
	
	public FiltroDecorador(Filtro filtro) {
		this.filtroDecorador = filtro;
	}
	
    public String informarFiltros() {
        return filtroDecorador.informarFiltros();
    }

	public Filtro getFiltro() {
		return filtroDecorador;
	}
}
