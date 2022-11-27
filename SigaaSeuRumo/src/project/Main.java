package project;

public class Main {

	public static void main(String[] args) {
		Aluno a = new Aluno();
		a.setUsuario("igor");
		a.setMatricula(12345);
		a.setSenha("senhadoaluno");
		
		String filtro = a.filtrarDisciplinas("Semestre, Curso");
		
		Filtro f = new FiltroPadrao();
		
		if(filtro.indexOf("Curso") != -1) {
			f= new FiltroCurso(f);	
		}
		if(filtro.indexOf("Semestre") != -1){
			f= new FiltroSemestre(f);
		}
		System.out.println(f.informarFiltros());
	}

}
