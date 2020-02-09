import java.io.*;
import java.util.regex.*;

public class Project02 {
	
	public static boolean check(String x1, String x2) {
		String[] labels_0 = {"INDI", "FAM", "HEAD", "TRLR", "NOTE"};
		String[] labels_1 = {"NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"};
		
		if (x1.equals("0")) {
			for (String s : labels_0)
				if (x2.equals(s))
					return true;
		}
		
		if (x1.equals("1")) {
			for (String s : labels_1)
				if (x2.equals(s))
					return true;
		}
		
		if (x1.equals("2")) {
			if (x2.equals("DATE"))
				return true;
		}
		return false;
	}

	public static void main(String[] args) throws IOException {
		String filename = args[0];
		BufferedReader br = new BufferedReader(new FileReader(new File(filename)));
		Pattern p = Pattern.compile("(\\d+)\\s+(\\w+)(?:[\\t ]+(.+))?");
		Matcher m;
		File output = new File(filename.substring(0, filename.indexOf('.')) + "_output.txt");		
		output.createNewFile();
		BufferedWriter bw = new BufferedWriter(new FileWriter(output.getName()));
		
		String line, level, tag, arg;
		char valid = 0;
		while ((line = br.readLine()) != null) {
			m = p.matcher(line);
			System.out.println("-->" + line);
			bw.write("-->" + line);
			bw.newLine();
			if (m.find()) {
				level = m.group(1);
				tag = m.group(2);
				arg = m.group(3);
				//===================== PROCESSING ========================
				if (tag.equals("INDI") || tag.equals("FAM")) {
					valid = 'N';
				}
				else {
					if (arg != null) {
						if (arg.equals("INDI") || arg.equals("FAM")) {
							//switch tag and arg
							String temp = tag;
							tag = arg;
							arg = temp;
						}
					}
					valid = check(level, tag) ? 'Y' : 'N';
				}
				//==========================================================
				System.out.print("<--" + level + "|" + tag + "|" + valid + "|");
				bw.write("<--" + level + "|" + tag + "|" + valid + "|");
				if (arg != null) {
					System.out.print(arg);
					bw.write(arg);
				}
				System.out.println();
				bw.newLine();
			}
		}
		br.close();
		bw.close();
	}

}
