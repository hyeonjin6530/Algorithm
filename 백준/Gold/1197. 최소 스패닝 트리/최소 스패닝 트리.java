import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.PriorityQueue;

class Edge implements Comparable<Edge>{
    int u, v, c;

    public Edge(int u, int v, int c){
        this.u = u;
        this.v = v;
        this.c = c;
    }

    @Override
    public int compareTo(Edge other) {
        if(this.c != other.c){
            return Integer.compare(this.c, other.c);
        }
        else if(this.u != other.u){
            return Integer.compare(this.u, other.u);
        }
        else{
            return Integer.compare(this.v, other.v);
        }
        
    }
    
}

public class Main {

    static int[] parent;

    public static int find(int u){
        int r = u;

        while(parent[r] != r){
            r = parent[r];
        }

        while(parent[u] != u){
            int tmp = parent[u];
            parent[u] = r;
            u = tmp; 
        }
        return r;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        parent = new int[n+1];

        for(int i = 0; i<n+1; i++){
            parent[i] = i;
        }

        ArrayList<Edge> edgeList = new ArrayList<>();
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            
            edgeList.add(new Edge(u, v, c));
        }

        PriorityQueue<Edge> edges = new PriorityQueue<>(edgeList);

        int total_cost = 0;
        int num_edges = 0;

        while(!edges.isEmpty()){
            Edge e = edges.poll();

            int ur = find(e.u);
            int vr = find(e.v);

            if(ur != vr){
                total_cost += e.c;
                num_edges += 1;
                parent[ur] = vr;
            }
            
            if(num_edges >= n-1) break; 
       }

       br.close();

       System.out.println(total_cost);
    }
}
