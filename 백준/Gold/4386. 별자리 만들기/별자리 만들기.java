import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.PriorityQueue;

class Edge implements Comparable<Edge>{
    int u, v;
    double c;

    public Edge(int u, int v, double c){
        this.u = u;
        this.v = v;
        this.c = c;
    }

    @Override
    public int compareTo(Edge other) {
        if(this.c != other.c){
            return Double.compare(this.c, other.c);
        }
        else if(this.u != other.u){
            return Integer.compare(this.u, other.u);
        }
        else{
            return Integer.compare(this.v, other.v);
        }
        
    }
    
}

class Star{
    int num;
    double x;
    double y;

    Star(int num, double x, double y){
        this.num = num;
        this.x = x;
        this.y = y;
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
        int n = Integer.parseInt(br.readLine());  // 별의 개수

        StringTokenizer st;

        ArrayList<Star> starList = new ArrayList<>();
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            double x = Double.parseDouble(st.nextToken());
            double y = Double.parseDouble(st.nextToken());

            starList.add(new Star(i, x, y));
        }

        ArrayList<Edge> edgeList = new ArrayList<>();
        for(int i = 0; i < n; i++){
            for(int j = i+1; j<n; j++){
                double dist = Math.sqrt(Math.pow(starList.get(i).x - starList.get(j).x, 2) + Math.pow(starList.get(i).y - starList.get(j).y, 2));
                edgeList.add(new Edge(i, j, dist));
            }
        }

        PriorityQueue<Edge> edges = new PriorityQueue<>(edgeList);

        parent = new int[n];

        for(int i = 0; i<n; i++){
            parent[i] = i;
        }

        double total_cost = 0;
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

       System.out.printf("%.2f", total_cost);
    }
}


