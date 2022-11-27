package project;

public class Aluno {
	private int matricula;
	private String usuario;
	private String senha;
	public String semestre_atual;
	public String disciplinas_cursadas[];
	
	public int getMatricula() {
		return matricula;
	}

	public void setMatricula(int matricula) {
		this.matricula = matricula;
	}
	
	public String getUsuario() {
		return usuario;
	}
	
	public void setUsuario(String usuario) {
		this.usuario =usuario;
	}
	
	public String getSenha() {
		return senha;
	}
	
	public void setSenha(String senha) {
		this.senha = senha;
	}
	
	/*Deve ser informado uma string com os filtros e usa o FiltroDecorador*/
	public String filtrarDisciplinas(String filtro) {
		return filtro;
	}

	public Object visualizarDisciplinas() {
		
		return null;
	}
	
}
