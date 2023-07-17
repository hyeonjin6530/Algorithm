import java.util.PriorityQueue;
import java.util.ArrayList;
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {  // 우선순위 큐에 도시와 비용을 저장하기 위함
    int idx;
    int weight;
 
    public Node(int idx, int weight) {
        this.idx = idx;
        this.weight = weight;
    }
 
    @Override
    public int compareTo(Node w) {
        // return weight - node.weight;
        return Integer.compare(this.weight, w.weight);
    }
 
}

public class Main {
    static int v, e;
    static int[] cost; 
    static ArrayList<ArrayList<Node>> graph;
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer c;  // 문자열 쪼개기

        c = new StringTokenizer(br.readLine());
        v = Integer.parseInt(c.nextToken());
        e = Integer.parseInt(c.nextToken());
 
        cost = new int[v+1];

        int INF = Integer.MAX_VALUE;
        Arrays.fill(cost, INF);
 
        graph = new ArrayList<>();
        for (int i = 0; i <= v; i++) graph.add(new ArrayList<>());

        int start = Integer.parseInt(br.readLine());

        for (int i = 0; i < e; i++) {
            c = new StringTokenizer(br.readLine());
            int start_num = Integer.parseInt(c.nextToken());
            int end_num = Integer.parseInt(c.nextToken());
            int money = Integer.parseInt(c.nextToken());
 
            graph.get(start_num).add(new Node(end_num, money));
        }

        int[] result = dijkstra(start);

        for(int i = 1; i < v+1; i++){
            if(result[i] == INF) bw.write("INF \n" );
            else bw.write(result[i] + "\n");
        }; 

        bw.close();
        br.close();
    }
 
    public static int[] dijkstra(int start) {  // 다익스트라 알고리즘
        cost[start] = 0;
        PriorityQueue<Node> p_queue = new PriorityQueue<>();
        p_queue.offer(new Node(start, 0));

        boolean[] check;
        check = new boolean[v+1];
 
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
        return cost;
    }
}
