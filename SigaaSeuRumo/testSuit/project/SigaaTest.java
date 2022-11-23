package project;

import static org.junit.Assert.assertTrue;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class SigaaTest {
	
	Aluno aluno;
	Disciplina disciplina;
	Campus campus;
	
	public void setUp() throws Exception {
		disciplina = new Disciplina("Calculo diferencial e integral 1");
		
	}
	
	public void testAddDisciplina() {
		campus.cadastrarDisciplina(disciplina);
		
		boolean achou = false;
		for (Disciplina d : campus.getDisciplinas()) {
			if (d.codigo == disciplina.codigo)
				achou = true;
		}
		assertTrue(achou);
	}
	
	public void testRemoverDisciplina() {
		campus.removerDisciplina(disciplina.codigo);
		
		boolean removeu = true;
		for (Disciplina d : campus.getDisciplinas()) {
			if (d.codigo == disciplina.codigo)
				removeu = false;
		}
		assertTrue(removeu);
	}
	
	public void testVisualizarDisciplinas() {
		retornoDisciplinas = aluno.visualizarDisciplinas();
		
		classeRetorno = retornoDisciplinas.getClass().getSimpleName();
		 
		boolean retornou = false;
		if(classeRetorno == "ArrayList") {
			retornou = true;
		}
		 
		assertTrue(retornou);
	}
	
	public void testFiltrarDisciplinas(ArrayList filtros) {
		retornoDisciplinas = aluno.filtrarDisciplinas();
		
		classeRetorno = retornoDisciplinas.getClass().getSimpleName();
		
		boolean retornou = false;
		if(classeRetorno == "ArrayList") {
			retornou = true;
		}
		 
		assertTrue(retornou);
	}
	
	@Test
	void test() {
		
		
		fail("Not yet implemented");
	}

}
