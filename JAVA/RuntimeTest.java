import java.io.*;

public class RuntimeTest
{
    public static void main(String[] args)
    {
        try
        {
            Runtime r = Runtime.getRuntime();
            Process p = Runtime.getRuntime().exec("/home/ravi/Documents/PYCODERS/ENGLISH/Countrys.py");
            p.waitFor();
            BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line = "";
            while ((line = br.readLine()) != null)
            {
                System.out.println(line);
            }
            p.waitFor();

        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}