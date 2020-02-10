import java.io.*;
import java.util.regex.*;
import java.util.ArrayList;
import java.util.HashMap;

class Date {
	int day, month, year;
	
	public Date() {
		day = 0; month = 0; year = 0; //this will stand as an unspecified date
	}
	
	public Date(String x) {
		Pattern p = Pattern.compile("(\\d+) (\\w{3}) (\\d+)");
		Matcher m = p.matcher(x);
		String[] months = {"JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"};
		
		if (m.find()) {
			day = Integer.parseInt(m.group(1));
			year = Integer.parseInt(m.group(3));
			month = 0; //if this remains 0, there was an error
			
			for (int i = 0; i < months.length; i++)
				if (m.group(2).equals(months[i]))
					month = i + 1;
		}
	}
	
	public int getDay() {
		return day;
	}
	
	public int getMonth() {
		return month;
	}
	
	public int getYear() {
		return year;
	}
	
	public String toString() {
		if (day == 0) {
			return "N/A";
		}
		return year + "-" + month + "-" + day;
	}
}

class Individual {
	Date birthday, death;
	String name, child_family, spouse_family;
	char gender;
	boolean birthday_flag, death_flag;
	
	public Individual() {
		name = "???";
		child_family = "N/A";
		spouse_family = "N/A";
		birthday_flag = false;
		death_flag = false;
		death = new Date();
		birthday = new Date();
	}
	
	public void accept_level_1(int tag_id, String arg) {
		switch(tag_id) {
		case 0: //tag is "NAME"
			name = arg;
			break;
		case 1: //tag is "SEX"
			gender = arg.charAt(0);
			break;
		case 2: //tag is "BIRT"
			birthday_flag = true;
			break;
		case 3: //tag is "DEAT"
			death_flag = true;
			break;
		case 4: //tag is "FAMC"
			child_family = arg;
			break;
		case 5: //tag is "FAMS"
			spouse_family = arg;
			break;
		default:
			
		}
	}
	
	public void accept_date(String arg) {
		if (birthday_flag) {
			birthday = new Date(arg);
			birthday_flag = false;
			return;
		}
		if (death_flag) {
			death = new Date(arg);
			death_flag = false;
			return;
		}
	}
	
	public boolean isAlive() {
		if (death.getDay() == 0)
			return false;
		return true;
	}
	
	public int getAge() {
		//current day set as 2/9/2020
		int age = 2020 - birthday.getYear();
		if (birthday.getMonth() >= 2 && birthday.getDay() >= 9)
			return age;
		return age - 1;
	}
}

class Family {
	Date married, divorce;
	String husb_id, wife_id;
	ArrayList<String> children = new ArrayList<>();
	boolean married_flag, divorce_flag;
	
	public Family() {
		married = new Date();
		divorce = new Date();
		husb_id = "N/A";
		wife_id = "N/A";
		married_flag = divorce_flag = false;
	}
	
	public void accept_level_1(int tag_id, String arg) {
		switch(tag_id) {
		case 6: //tag is "MARR"
			married_flag = true;
			break;
		case 7: //tag is "HUSB"
			husb_id = arg;
			break;
		case 8: //tag is "WIFE"
			wife_id = arg;
			break;
		case 9: //tag is "CHIL"
			children.add(arg);
			break;
		case 10: //tag is "DIV"
			divorce_flag = true;
			break;
		default:
			
		}
	}
	
	public void accept_date(String arg) {
		if (married_flag) {
			married = new Date(arg);
			married_flag = false;
			return;
		}
		if (divorce_flag) {
			divorce = new Date(arg);
			divorce_flag = false;
			return;
		}
	}
	
	public void printChildren() {
		for (int i = 0; i < children.size(); i++)
			System.out.print(children.get(i) + " ");
		System.out.println();
	}
}


public class Project03 {
	
	public static int check(String x1, String x2) {
		String[] labels_0 = {"INDI", "FAM", "HEAD", "TRLR", "NOTE"};
		String[] labels_1 = {"NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"};
		
		if (x1.equals("0")) {
			for (int i = 0; i < labels_0.length; i++)
				if (x2.equals(labels_0[i]))
					return i;
		}
		
		if (x1.equals("1")) {
			for (int i = 0; i < labels_1.length; i++)
				if (x2.equals(labels_1[i]))
					return i;
		}
		
		if (x1.equals("2")) {
			if (x2.equals("DATE"))
				return 0;
		}
		return -1;
	}

	public static void main(String[] args) throws IOException {
		String filename = args[0];
		BufferedReader br = new BufferedReader(new FileReader(new File(filename)));
		Pattern p = Pattern.compile("(\\d+)\\s+(\\w+)(?:[\\t ]+(.+))?");
		Matcher m;
		HashMap<String, Individual> individuals = new HashMap<>();
		HashMap<String, Family> families = new HashMap<>();		
		
		String line, level, tag, arg;
		char valid = 0;
		int fam_indi_flag = 0; //0 for neither, 1 for fam, 2 for individual
		String current_id = "none"; //the current id of the family/individual
		int tag_id = -1; //id of tag, -1 if invalid tag
		
		while ((line = br.readLine()) != null) {
			m = p.matcher(line);
			if (m.find()) {
				level = m.group(1);
				tag = m.group(2);
				arg = m.group(3);
				//===================== PARSING ========================
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
					valid = (tag_id = check(level, tag)) >= 0 ? 'Y' : 'N';
				}
				//================== PROCESSING ========================
				if (valid == 'Y') { //statement is valid
					if (level.equals("0")) { //level 0
						switch(tag_id) {
						case 0: //tag is "INDI"
							fam_indi_flag = 2; //set flag to individual
							individuals.put(arg, new Individual()); //create an individual in the hashmap
							current_id = arg;
							break;
						case 1: //tag is "FAM"
							fam_indi_flag = 1; //set flag to family
							families.put(arg, new Family()); //create a family in the hashmap
							current_id = arg;
							break;
						default:
							fam_indi_flag = 0;
							current_id = "none";
						}
					}
					
					else if (level.equals("1")) { //level 1
						if (fam_indi_flag == 1) { // family operations
							families.get(current_id).accept_level_1(tag_id, arg);
						}
						else if (fam_indi_flag == 2) { // individual operations
							individuals.get(current_id).accept_level_1(tag_id, arg);
						}
					}
					
					else if (level.equals("2")) { //level 2 (tag is "DATE")
						if (fam_indi_flag == 1) { // family dates
							families.get(current_id).accept_date(arg);
						}
						else if (fam_indi_flag == 2) { // individual dates
							individuals.get(current_id).accept_date(arg);
						}
					}
					else
						System.out.println("ERROR: level out of range");
				}
			}
		}
		//=========================== PRINTING ===============================
		System.out.println("Individuals");
		System.out.println("ID\tName\t\tGender\tBirthday\tAge\tAlive\tDeath\t\tChild\tSpouse");
		
		for (String x : individuals.keySet())
			System.out.println(x + "\t" + individuals.get(x).name + "\t" + individuals.get(x).gender + "\t" + individuals.get(x).birthday + "\t" + individuals.get(x).getAge() + "\t" + individuals.get(x).isAlive() + "\t" + individuals.get(x).death + "\t" + individuals.get(x).child_family + "\t" + individuals.get(x).spouse_family);
		
		System.out.println();
		System.out.println("Families");
		System.out.println("ID\tMarried\t\tDivorced\tHusband ID\tHusband Name\tWife ID\tWife Name\t\tChildren");
		
		for (String x : families.keySet()) {
			System.out.print(x + "\t" + families.get(x).married + "\t" + families.get(x).divorce + "\t\t" + families.get(x).husb_id + "\t\t" + individuals.get(families.get(x).husb_id).name + "\t" + families.get(x).wife_id + "\t" + individuals.get(families.get(x).wife_id).name + "\t");
			families.get(x).printChildren();
		}
		
		br.close();
	}

}
