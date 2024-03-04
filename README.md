<div align="center">
  <h1>PROCESSO SELETIVO - TESTE PRÁTICO LABSYSTEM</h1><br>
</div>
<br>
<div align="center">
  <h3><ul>
  <li>Desenvolver uma tela de cadastro de produtos com CRUD (Create, Read, Update, Delete) </li>
</ul></h3><br><br>

</div>

---

<br>

<ul>
  <li><h2>Scripts SQL para criação do Banco e tabela produto</h2></li> 
</ul>

<h4>Código para criar o banco de dados:</h4>

<i><p>CREATE DATABASE `bdcadastro`;</p></i><br>

<h4>Código para criar tabela produto:</h4>

<i><p>CREATE TABLE `bdcadastro`.`produto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NULL,
  `data_cadastro` DATETIME NULL,
  `descricao` MEDIUMTEXT NULL,
  `nome_usuario` VARCHAR(45) NULL,
  `quantidade` INT NULL,
  `valor` DECIMAL NULL,
  PRIMARY KEY (`id`));</p></i><br>

<h4>Opcional: </h4>

<i><p>INSERT INTO `bdcadastro`.`produto` (`id`, `nome`, `data_cadastro`, `descricao`, `nome_usuario`, `quantidade`, `valor`) VALUES ('1', 'Teclado', '2024-03-03 00:00:00', 'Dell', 'Robson', '5', '80');
</p></i><br>

<h4>Você pode usar o banco de dados de sua preferência para executar o projeto, para isso, basta fazer umas configurações antes.</h4><br>


<img src="https://github.com/gabrieldossant/Teste-LabSystem/assets/80858391/6d4e13c5-15c2-45f7-b531-41c9a6934e82">


<ul>
  <li><i>Configure o <b>import</b> e a <b>conexão</b> no arquivo banco.py com o banco de dados que vocè estiver usando. </i></li>
</ul><br><br><br>

<div align="center">
  <h5>Feito 100% em Python com conexão com o banco de dados MySQL Workbench 8.0</h5>
</div>
