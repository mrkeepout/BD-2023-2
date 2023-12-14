CREATE TABLE Recursos (
    Estado_conservacao VARCHAR,
    Data_aquisicao DATE,
    Localizacao_fisica VARCHAR,
    Categoria VARCHAR,
    Descricao VARCHAR,
    ID INTEGER PRIMARY KEY,
    fk_mat_didat_ID INTEGER,
    fk_Livros_ISBN VARCHAR
);

CREATE TABLE Usuarios (
    ID_user INTEGER PRIMARY KEY,
    Nome VARCHAR,
    Sobrenome VARCHAR,
    Login VARCHAR,
    Senha VARCHAR,
    URI_foto_user VARCHAR,
    Funcao VARCHAR
);

CREATE TABLE Livros (
    ISBN VARCHAR PRIMARY KEY,
    URI_capa_livro VARCHAR,
    Autor VARCHAR,
    Titulo VARCHAR
);

CREATE TABLE Materiais_didaticos (
    ID_mat_didat INTEGER PRIMARY KEY,
    URI_foto_material VARCHAR,
    Numero_serie VARCHAR
);

CREATE TABLE _Emprestimo (
    Data_emprestimo DATE,
    Data_devolucao_prevista DATE,
    Status_emp VARCHAR,
    fk_Recursos_ID_Item INTEGER,
    fk_Usuarios_ID_user INTEGER
);
 
ALTER TABLE Recursos ADD CONSTRAINT FK_Recursos_2
    FOREIGN KEY (fk_mat_didat_ID)
    REFERENCES Materiais_didaticos (ID_mat_didat)
    ON DELETE SET NULL;
 
ALTER TABLE Recursos ADD CONSTRAINT FK_Recursos_3
    FOREIGN KEY (fk_Livros_ISBN)
    REFERENCES Livros (ISBN)
    ON DELETE SET NULL;
 
ALTER TABLE _Emprestimo ADD CONSTRAINT FK__Emprestimo_1
    FOREIGN KEY (fk_Recursos_ID_Item)
    REFERENCES Recursos (ID);
 
ALTER TABLE _Emprestimo ADD CONSTRAINT FK__Emprestimo_2
    FOREIGN KEY (fk_Usuarios_ID_user)
    REFERENCES Usuarios (ID_user);