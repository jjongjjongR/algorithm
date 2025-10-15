import java.io.*;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String ip = "";

        while((ip = br.readLine()) != null) {
            String[] num = ip.split(" ");
            int A = Integer.parseInt(num[0]);
            int B = Integer.parseInt(num[1]);
            
            bw.write((A+B) + "\n");
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
}