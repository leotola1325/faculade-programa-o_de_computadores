import java.util.*;

public class Loja {

    static Map<String, Map<String, Object>> produtos = new LinkedHashMap<>();
    static List<Map<String, Object>> carrinho = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        carregarProdutos();
        menu();
    }

    static void carregarProdutos() {
        produtos.put("1",  criarProduto("Arroz 5kg",          25.90));
        produtos.put("2",  criarProduto("Feijao 1kg",          8.50));
        produtos.put("3",  criarProduto("Macarrao 500g",        4.75));
        produtos.put("4",  criarProduto("Azeite 500ml",        22.00));
        produtos.put("5",  criarProduto("Leite 1L",             5.99));
        produtos.put("6",  criarProduto("Cafe 500g",           15.90));
        produtos.put("7",  criarProduto("Acucar 1kg",           4.49));
        produtos.put("8",  criarProduto("Manteiga 200g",        9.80));
        produtos.put("9",  criarProduto("Farinha 1kg",          6.30));
        produtos.put("10", criarProduto("Oleo de soja 900ml",   7.99));
    }

    static Map<String, Object> criarProduto(String nome, double preco) {
        Map<String, Object> produto = new HashMap<>();
        produto.put("nome", nome);
        produto.put("preco", preco);
        return produto;
    }

    static void exibirProdutos() {
        System.out.println("\n===== PRODUTOS =====");
        for (Map.Entry<String, Map<String, Object>> entry : produtos.entrySet()) {
            String cod = entry.getKey();
            String nome = (String) entry.getValue().get("nome");
            double preco = (double) entry.getValue().get("preco");
            System.out.printf("  [%2s] %-25s R$ %.2f%n", cod, nome, preco);
        }
        System.out.println("====================");
    }

    static void exibirCarrinho() {
        if (carrinho.isEmpty()) {
            System.out.println("\n  Carrinho vazio.");
            return;
        }
        System.out.println("\n===== CARRINHO =====");
        double total = 0;
        for (Map<String, Object> item : carrinho) {
            String nome = (String) item.get("nome");
            double preco = (double) item.get("preco");
            System.out.printf("  - %-25s R$ %.2f%n", nome, preco);
            total += preco;
        }
        System.out.println("--------------------");
        System.out.printf("  %-25s R$ %.2f%n", "TOTAL", total);
        System.out.println("====================");
    }

    static void adicionarProduto() {
        exibirProdutos();
        System.out.print("\nDigite o numero do produto: ");
        String codigo = scanner.nextLine().trim();

        if (produtos.containsKey(codigo)) {
            Map<String, Object> item = produtos.get(codigo);
            carrinho.add(item);
            System.out.println("\n  OK! '" + item.get("nome") + "' adicionado!");
        } else {
            System.out.println("\n  Produto nao encontrado.");
        }
    }

    static void finalizarCompra() {
        if (carrinho.isEmpty()) {
            System.out.println("\n  Carrinho vazio.");
            return;
        }
        exibirCarrinho();
        System.out.println("\n  Obrigado pela compra!");
    }

    static void menu() {
        while (true) {
            System.out.println("\n[1] Ver produtos");
            System.out.println("[2] Adicionar");
            System.out.println("[3] Ver carrinho");
            System.out.println("[4] Finalizar");
            System.out.println("[0] Sair");
            System.out.print("Escolha: ");

            String opcao = scanner.nextLine().trim();

            switch (opcao) {
                case "1":
                    exibirProdutos();
                    break;
                case "2":
                    adicionarProduto();
                    break;
                case "3":
                    exibirCarrinho();
                    break;
                case "4":
                    finalizarCompra();
                    return;
                case "0":
                    System.out.println("\n  Ate mais!");
                    return;
                default:
                    System.out.println("\n  Opcao invalida.");
                    break;
            }
        }
    }
}