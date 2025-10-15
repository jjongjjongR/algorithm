import java.io.*;

class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());

        for(int i = 0 ; i < T ; i++){
            String line = br.readLine();
            String[] part = line.split(" ");

            int A = Integer.parseInt(part[0]);
            int B = Integer.parseInt(part[1]);

            bw.write((A + B) + "\n");
        }
        bw.close();
        br.close();
    }
}