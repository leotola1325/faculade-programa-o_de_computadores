const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());
app.use(express.static("public"));

const db = new sqlite3.Database("database.db");

// Criar tabelas
db.run(`
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    senha TEXT
)`);

db.run(`
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL
)`);

// Cadastro
app.post("/cadastro", (req, res) => {
    const { usuario, senha } = req.body;
    db.run("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", [usuario, senha]);
    res.send("Usuário cadastrado!");
});

// Login
app.post("/login", (req, res) => {
    const { usuario, senha } = req.body;

    db.get(
        "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?",
        [usuario, senha],
        (err, row) => {
            if (row) {
                res.json({ sucesso: true });
            } else {
                res.json({ sucesso: false });
            }
        }
    );
});

// Listar produtos
app.get("/produtos", (req, res) => {
    db.all("SELECT * FROM produtos", [], (err, rows) => {
        res.json(rows);
    });
});

// Iniciar servidor
app.listen(3000, () => {
    console.log("Servidor rodando em http://localhost:3000");
});