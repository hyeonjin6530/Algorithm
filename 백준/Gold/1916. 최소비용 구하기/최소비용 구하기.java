import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

class Node implements Comparable<Node> {  // 우선순위 큐에 도시와 비용을 저장하기 위함
    int idx;
    int weight;
 
    public Node(int idx, int weight) {
        this.idx = idx;
        this.weight = weight;
    }
 
    @Override
    public int compareTo(Node other) {
        return Integer.compare(this.weight, other.weight);
    }
 
}

public class Main{
    static int n, m;
    static boolean[] visit; // 도시를 방문했는지 체크하기 위함
    static int[] cost; // 버스 비용들을 저장
    static ArrayList<ArrayList<Node>> graph;
 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
 
        visit = new boolean[n + 1];
        cost = new int[n + 1];

        int INF = Integer.MAX_VALUE;
        Arrays.fill(cost, INF);
 
        graph = new ArrayList<>();
        for (int i=0; i <= n; i++) graph.add(new ArrayList<>());
 
        StringTokenizer c;  // 문자열 쪼개기
        for (int i=0; i < m; i++) {
            c = new StringTokenizer(br.readLine());
            int start_num = Integer.parseInt(c.nextToken());
            int end_num = Integer.parseInt(c.nextToken());
            int money = Integer.parseInt(c.nextToken());
 
            graph.get(start_num).add(new Node(end_num, money));
        }
 
        c = new StringTokenizer(br.readLine());
        int start_city = Integer.parseInt(c.nextToken());
        int end_city = Integer.parseInt(c.nextToken());

        int result = dijkstra(start_city, end_city); 
 
        System.out.println(result);
        br.close();
    }
 
    public static int dijkstra(int start_city, int end_city) {  // 다익스트라 알고리즘
        cost[start_city] = 0;
        PriorityQueue<Node> p_queue = new PriorityQueue<>();
        p_queue.offer(new Node(start_city, 0));

        boolean[] check;
        check = new boolean[n + 1];
 
        while (!p_queue.isEmpty()) {  // 큐가 빌 때까지 반복
            int now = p_queue.poll().idx;

            if (!check[now]) {
                check[now] = true;

                for (Node node : graph.get(now)) {
                    if (cost[node.idx] > cost[now] + node.weight) {
                        cost[node.idx] = cost[now] + node.weight;
                        p_queue.offer(new Node(node.idx, cost[node.idx]));
                    }
                }
            }
        }
        return cost[end_city];
    }
}
