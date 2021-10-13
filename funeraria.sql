-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 13-Out-2021 às 17:10
-- Versão do servidor: 10.4.20-MariaDB
-- versão do PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `funeraria`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `contratos`
--

CREATE TABLE `contratos` (
  `ID` int(11) NOT NULL,
  `CLIENTE` varchar(255) NOT NULL,
  `PAGINA` int(11) NOT NULL,
  `CONTRATO` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tcliente`
--

CREATE TABLE `tcliente` (
  `ID` int(11) NOT NULL,
  `NOME` varchar(255) NOT NULL,
  `RG` varchar(36) NOT NULL,
  `CPF` varchar(36) NOT NULL,
  `TELEFONE` varchar(36) NOT NULL,
  `EMAIL` varchar(255) NOT NULL,
  `DATANASCIMENTO` date NOT NULL,
  `NATURALIDADE` varchar(36) NOT NULL,
  `ENDERECO` varchar(255) NOT NULL,
  `COMPLEMENTO` varchar(255) NOT NULL,
  `BAIRRO` varchar(255) NOT NULL,
  `CIDADE` varchar(255) NOT NULL,
  `UF` varchar(255) NOT NULL,
  `CEP` varchar(255) NOT NULL,
  `PAIS` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `tcliente`
--

INSERT INTO `tcliente` (`ID`, `NOME`, `RG`, `CPF`, `TELEFONE`, `EMAIL`, `DATANASCIMENTO`, `NATURALIDADE`, `ENDERECO`, `COMPLEMENTO`, `BAIRRO`, `CIDADE`, `UF`, `CEP`, `PAIS`) VALUES
(2, 'Novo Cliente', '123456789', '987654321', '(55) 9 1234-5678', 'email@email.com', '0000-00-00', 'Naturalidade', 'Endereço', 'Complemento', 'Bairro', 'Cidade', 'Uf', '123456789', 'Brasil');

-- --------------------------------------------------------

--
-- Estrutura da tabela `testoque`
--

CREATE TABLE `testoque` (
  `ID` int(11) NOT NULL,
  `PRODUTO` varchar(255) NOT NULL,
  `CODBARRAS` varchar(36) NOT NULL,
  `UNIDADE` varchar(36) NOT NULL,
  `PRECOCUSTO` decimal(10,0) NOT NULL,
  `PRECOVENDA` decimal(10,0) NOT NULL,
  `QTDE` decimal(10,0) NOT NULL,
  `NCM` varchar(36) NOT NULL,
  `TRIBUTACAOIPI` decimal(10,0) NOT NULL,
  `TRIBUTACAOPIS` decimal(10,0) NOT NULL,
  `CSOSN` varchar(36) NOT NULL,
  `TRIBUTACAOCOFINS` decimal(10,0) NOT NULL,
  `VALORICMSST` decimal(10,0) NOT NULL,
  `VALORIPI` decimal(10,0) NOT NULL,
  `TIPOBARRA` varchar(36) NOT NULL,
  `GRUPO` varchar(36) NOT NULL,
  `FORNECEDOR` varchar(255) NOT NULL,
  `TAMANHO` decimal(10,0) NOT NULL,
  `PESO` decimal(10,0) NOT NULL,
  `QTDEMINIMA` decimal(10,0) NOT NULL,
  `QTDEMAXIMA` decimal(10,0) NOT NULL,
  `DATAULTIMAVENDA` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `testoque`
--

INSERT INTO `testoque` (`ID`, `PRODUTO`, `CODBARRAS`, `UNIDADE`, `PRECOCUSTO`, `PRECOVENDA`, `QTDE`, `NCM`, `TRIBUTACAOIPI`, `TRIBUTACAOPIS`, `CSOSN`, `TRIBUTACAOCOFINS`, `VALORICMSST`, `VALORIPI`, `TIPOBARRA`, `GRUPO`, `FORNECEDOR`, `TAMANHO`, `PESO`, `QTDEMINIMA`, `QTDEMAXIMA`, `DATAULTIMAVENDA`) VALUES
(1, 'Teste', '123456789', 'UN', '1', '1', '99968', '123456789', '1', '1', '1', '1', '1', '1', '1', 'GRUPO', 'FORNECEDOR', '1', '1', '1', '999999', '2021-10-13 12:07:56');

-- --------------------------------------------------------

--
-- Estrutura da tabela `tfalecido`
--

CREATE TABLE `tfalecido` (
  `ID` int(11) NOT NULL,
  `DOCUMENTO` int(11) NOT NULL,
  `NOME` varchar(255) NOT NULL,
  `CPF` varchar(36) NOT NULL,
  `RG` varchar(36) NOT NULL,
  `ENDERECO` varchar(255) NOT NULL,
  `DATANASCIMENTO` varchar(36) NOT NULL,
  `FALECIDOEM` varchar(255) NOT NULL,
  `HORAOBITO` varchar(255) NOT NULL,
  `SEPULTADOEM` varchar(255) NOT NULL,
  `LOCALOBITO` varchar(255) NOT NULL,
  `MEDICO` varchar(255) NOT NULL,
  `CEMITERIO` varchar(255) NOT NULL,
  `CONTRATANTE` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tfornecedor`
--

CREATE TABLE `tfornecedor` (
  `ID` int(11) NOT NULL,
  `RAZAOSOCIAL` varchar(255) NOT NULL,
  `NOMEFANTASIA` varchar(255) NOT NULL,
  `CNPJ` varchar(36) NOT NULL,
  `IE` varchar(36) NOT NULL,
  `IM` varchar(36) NOT NULL,
  `ENDERECO` varchar(255) NOT NULL,
  `BAIRRO` varchar(255) NOT NULL,
  `CIDADE` varchar(255) NOT NULL,
  `PAIS` varchar(36) NOT NULL,
  `UF` varchar(5) NOT NULL,
  `CEP` varchar(36) NOT NULL,
  `COMPLEMENTO` varchar(255) NOT NULL,
  `TELEFONE` varchar(36) NOT NULL,
  `SAC` varchar(255) NOT NULL,
  `EMAIL` varchar(255) NOT NULL,
  `SITE` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `tfornecedor`
--

INSERT INTO `tfornecedor` (`ID`, `RAZAOSOCIAL`, `NOMEFANTASIA`, `CNPJ`, `IE`, `IM`, `ENDERECO`, `BAIRRO`, `CIDADE`, `PAIS`, `UF`, `CEP`, `COMPLEMENTO`, `TELEFONE`, `SAC`, `EMAIL`, `SITE`) VALUES
(1, 'Razão Social', 'Teste', '123456789', '123456789', '123456789', 'endereço', 'None', 'cidade', 'pais', 'uf', '123456789', 'complemento', '(55) 9 1234-5678', 'sac', 'email@email.com', 'www.site.com.br');

-- --------------------------------------------------------

--
-- Estrutura da tabela `treceber`
--

CREATE TABLE `treceber` (
  `ID` int(11) NOT NULL,
  `IDCLIENTE` int(11) NOT NULL,
  `QTDEPARCELA` int(11) NOT NULL,
  `NPARCELA` int(11) NOT NULL,
  `DATAVENCIMENTO` date NOT NULL,
  `VALORORIGINAL` decimal(10,0) NOT NULL DEFAULT 0,
  `VALORENTRADA` decimal(10,0) NOT NULL DEFAULT 0,
  `VALORASERPAGO` decimal(10,0) NOT NULL DEFAULT 0,
  `DATARECEBIMENTO` date NOT NULL,
  `QUITADA` enum('0','1') NOT NULL DEFAULT '0',
  `EXTORNADA` enum('0','1') NOT NULL DEFAULT '0',
  `DOCUMENTO` int(11) NOT NULL,
  `VALORESCRITO` varchar(255) NOT NULL,
  `VENDEDOR` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `contratos`
--
ALTER TABLE `contratos`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `tcliente`
--
ALTER TABLE `tcliente`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `testoque`
--
ALTER TABLE `testoque`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `tfalecido`
--
ALTER TABLE `tfalecido`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `tfornecedor`
--
ALTER TABLE `tfornecedor`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `treceber`
--
ALTER TABLE `treceber`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `contratos`
--
ALTER TABLE `contratos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tcliente`
--
ALTER TABLE `tcliente`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `testoque`
--
ALTER TABLE `testoque`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `tfalecido`
--
ALTER TABLE `tfalecido`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tfornecedor`
--
ALTER TABLE `tfornecedor`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `treceber`
--
ALTER TABLE `treceber`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
