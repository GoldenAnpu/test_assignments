<div align="center">
<h1> lingvanex </h1> 
</div>

### Technical task
В файле <a href="https://github.com/GoldenAnpu/test_assignments/blob/master/lingvanex/PythonTest.txt">PythonTest.txt</a> находятся строки с переводом английских слов на русские в формате
Astur-Leonese ; Asturian ; Asturian-Leonese ; Astur	астурийский ; астурлеонский

Это значит, что каждое из английских слов (Astur-Leonese ; Asturian ; Asturian-Leonese ; Astur) может переводиться как любое русское (астурийский ; астурлеонский)

Также встречаются простые варианты где в строке 1 английское и русское слово
Abidjan	Абиджан
 
Английские слова отделены от русских переводов символом табуляции

Надо распарсить этот файл и на базе него сделать 2 файла - English.txt и Russian txt, где каждой строке на английском будет соответствовать строка перевода на русском в другом файле во всех возможных вариантах.

Пример текста, который должен получиться в файлах, после работы вашего кода:

<table>
    <tr>
        <th>English.txt</th>
        <th>Russian.txt</th>	
    </tr>      
    <tr> 
        <td>Astur-Leonese</td>
        <td>астурийский</td>
    </tr>
    <tr>
        <td>Astur-Leonese</td>
        <td>астурлеонский</td>
    </tr>
    <tr>
        <td>Asturian</td>
        <td>астурийский</td>
    </tr>
    <tr>
        <td>Asturian</td>
        <td>астурлеонский</td>
    </tr>
    <tr>
        <td>Asturian-Leonese</td>
        <td>астурийский</td>
    </tr>
    <tr>
        <td>Asturian-Leonese</td>
        <td>астурлеонский</td>
    </tr>
    <tr>
        <td>....</td>
        <td>....</td>
    </tr>
</table>

### Solutions
 - <a href="https://github.com/GoldenAnpu/test_assignments/blob/master/lingvanex/parser_solution_1.py">parser_solution_1.py</a> - easier to read 🐣 ... as it seems to me.
 - <a href="https://github.com/GoldenAnpu/test_assignments/blob/master/lingvanex/parser_solution_2.py">parser_solution_2.py</a> - use more memory by storing prepared data in lists before writing, but more gracefully prepare output files.