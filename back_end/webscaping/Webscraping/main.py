from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
import re


def get_data_from_sigaa(login, senha):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://si3.ufc.br/")
        page.fill("input[name='user.login']", login)
        page.wait_for_timeout(750)
        page.fill("input[name='user.senha']", senha)
        page.wait_for_timeout(750)
        page.click("input[name='entrar']")
        page.wait_for_timeout(750)
        page.click("a[id='btnNaoResponderContinuar']")
        page.wait_for_timeout(750)
        page.click("input[id='btnSimLembrarQuestionario']")
        page.wait_for_timeout(750)
        page.click("input[type='submit']")
        page.wait_for_timeout(750)
        page.click("a[href='/sigaa/verPortalDiscente.do']")
        page.wait_for_timeout(750)
        page.click("tbody tr td:first-child")
        page.wait_for_timeout(750)
        page.click("tbody tr:nth-last-child(3)")
        page.wait_for_timeout(750)
        page.click("div[id='cmSubMenuID9'] tr:nth-child(2) td:nth-child(2)")
        page.wait_for_timeout(750)
        page.click("select[id='form:selectUnidade']")
        page.wait_for_timeout(750)
        page.select_option("select[id='form:selectUnidade']", value='959')
        page.wait_for_timeout(750)
        page.click("select[id='form:selectCurso']")
        page.wait_for_timeout(750)
        page.select_option("select[id='form:selectCurso']", value='657484')
        page.wait_for_timeout(2000)
        page.click("input[id='form:buttonBuscar']")
        page.wait_for_timeout(2000)
        inner = page.inner_html("table[id='lista-turmas']")
        inner.replace('\t', '').replace('\n', '')
        soup = BeautifulSoup(inner, 'html.parser')
        td = soup.select('tr')

        paragraphs = []
        for x in td:
            paragraphs.append(str(x))

        data = {}
        data['teste'] = paragraphs

        with open("testes.json", "w", encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False)

        browser.close()


def write_disciplines_data():
    sigaa_data = {
        'disciplinas': [],
        'professores': [],
        'horarios': []
    }

    # Abrindo os dados obtidos do SIGAA como HTML
    data = {}
    with open('testes.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Buscando as strings do html que fazem referência à disciplinas (possuem a class "destaque")
    paragraphs = data['teste']
    disciplinas_tags = list(filter(lambda k: 'class=\"destaque\"' in k, paragraphs))

    # Faz append de cada disciplina no dicionário "sigaa_data"
    for disciplina_tag in disciplinas_tags:
        disciplina = ''.join([c for c in disciplina_tag if c.isupper()])
        disciplina_nome = disciplina[3:-9]
        sigaa_data['disciplinas'].append(disciplina_nome)

    # Obtendo as sub strings que fazem referência aos dados da disciplina
    horarios_tags = list(filter(lambda k: 'style=\"font-size: xx-small\"' in k, paragraphs))

    # Obtendo os horários das disciplinas
    horarios_disciplinas = []
    for horario_tag in horarios_tags:
        horario_result = []
        horario_list = re.findall('<td>(.*?)<br/>', horario_tag)
        horario_str = ''.join(horario_list)
        horario_result.append(horario_str)

        horario_list = re.findall('<br/>(.*?)<br/>', horario_tag)
        horario_str = ''.join(horario_list)

        if horario_str != "":
            horario_result.append(horario_str)
            horario_tag = horario_tag.replace(f'<br/>{horario_str}', " ")

        horario_list = re.findall('<br/>(.*?)<br/>', horario_tag)
        horario_str = ''.join(horario_list)

        if horario_str != "":
            horario_result.append(horario_str)
            horario_tag = horario_tag.replace(f'<br/>{horario_str}', " ")

        horarios_disciplinas.append(horario_result)

    sigaa_data['horarios'] = horarios_disciplinas

    with open("sigaa_data.json", "w", encoding='utf-8') as outfile:
        json.dump(sigaa_data, outfile, ensure_ascii=False, indent=4)


def main():
    login = str(input('Digite seu login sigaa: '))
    senha = str(input('Digite sua senha sigaa: '))

    get_data_from_sigaa(login, senha)
    write_disciplines_data()


if __name__ == '__main__':
    main()
