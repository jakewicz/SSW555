import java.io.*;
import java.util.regex.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.time.LocalDateTime;

class Date {
	int day, month, year;
	
	public Date() {
		day = 0; month = 0; year = 0; //this will stand as an unspecified date
	}
	
	public Date(String x) {
		LocalDateTime now = LocalDateTime.now();
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
		
		//========== US01 ====================================
		if (year < now.getYear())
			return;
		
		if (year > now.getYear()) {
			System.out.println("Error: year is in the future");
			day = -1;
			return;
		}
		
		if (month > now.getMonthValue()) {
			System.out.println("Error: month is in the future");
			day = -1;
			return;
		}
		
		if (month < now.getMonthValue())
			return;
		
		if (day > now.getDayOfMonth()) {
			System.out.println("Error: day is in the future");
			day = -1;
		}
		//========================================================
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
	
	public boolean DateIsAfter(Date d) {
		if (day < 1)
			return false;
		
		if (d.day < 1)
			return false;
		
		if (year < d.year)
			return true;
		
		if (year > d.year)
			return false;
		
		if (month < d.month)
			return true;
		
		if (month > d.month)
			return false;
		
		if (day < d.day)
			return true;

			return false;
	}
	
	public String toString() {
		if (day == 0) {
			return "N/A";
		}
		else if (day == -1)
			return "invalid date: in future";
		
		else if (day == -2)
			return "married before birth";
		else if (day == -3)
			return "idied before birth";
		else if (day == -4)
			return "married before 14";
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
		LocalDateTime now = LocalDateTime.now();		
		int age = now.getYear() - birthday.getYear();
		if (birthday.getMonth() >= now.getMonthValue() && birthday.getDay() >= now.getDayOfMonth())
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
	public static String boolToString(boolean b) {
		if (b)
			return "true";
		return "false";
	}
	
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
		Scanner input = new Scanner(System.in);
		System.out.println("Enter filename: ");
		String filename = input.nextLine();
		BufferedReader br = new BufferedReader(new FileReader(new File("src/" + filename)));
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
		
		//========= US02 ==================
		for (String x : families.keySet()) {
			Date marr = families.get(x).married;
			Date bornh = individuals.get(families.get(x).husb_id).birthday;
			Date bornw = individuals.get(families.get(x).wife_id).birthday;
			
			if (marr.DateIsAfter(bornh))
				families.get(x).married.day = -2;

			if (marr.DateIsAfter(bornw))
				families.get(x).married.day = -2;
		}
		
		for (String x : individuals.keySet()) {
			//====================== US03 ===========================
			Date birth = individuals.get(x).birthday;
			Date death = individuals.get(x).death;
			if (death.DateIsAfter(birth))
				individuals.get(x).death.day = -3;
			
			//================== US10 ============================
			if (individuals.get(x).spouse_family != "N/A") {
				Date marr = families.get(individuals.get(x).spouse_family).married;
				birth.year += 14;
				if (marr.DateIsAfter(birth)) {
					marr.day = -4;
				}
			}
		}
		
		//=========================== PRINTING ===============================
		String[] arr = new String[9];
		System.out.println("Individuals");
		//System.out.println("ID\tName\t\tGender\tBirthday\tAge\tAlive\tDeath\t\tChild\tSpouse");
		String[] indititle = {"ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"};
		System.out.format("%-30s%-30s%-30s%-30s%-30s%-30s%-30s%-30s%-30s\n", indititle);
		
		for (String x : individuals.keySet()) {
			arr[0] = x;
			arr[1] = individuals.get(x).name;
			arr[2] = Character.toString(individuals.get(x).gender);
			arr[3] = individuals.get(x).birthday.toString();
			arr[4] = Integer.toString(individuals.get(x).getAge());
			arr[5] = boolToString(individuals.get(x).isAlive());
			arr[6] = individuals.get(x).death.toString();
			arr[7] = individuals.get(x).child_family;
			arr[8] = individuals.get(x).spouse_family;
			System.out.format("%-30s%-30s%-30s%-30s%-30s%-30s%-30s%-30s%-30s\n", arr);
			//System.out.println(individuals.get(x).spouse_family);
		}
		
		System.out.println();
		System.out.println("Families");
		String[] famtitle = {"ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"};
		System.out.format("%-30s%-30s%-30s%-30s%-30s%-30s%-30s%-30s\n", famtitle);
		//System.out.println("ID\tMarried\t\tDivorced\tHusband ID\tHusband Name\tWife ID\tWife Name\t\tChildren");
		
		for (String x : families.keySet()) {
			arr[0] = x;
			arr[1] = families.get(x).married.toString();
			arr[2] = families.get(x).divorce.toString();
			arr[3] = families.get(x).husb_id;
			arr[4] = individuals.get(families.get(x).husb_id).name;
			arr[5] = families.get(x).wife_id;
			arr[6] = individuals.get(families.get(x).wife_id).name;
			
			System.out.format("%-30s%-30s%-30s%-30s%-30s%-30s%-30s%-30s", arr);
			
			//System.out.print(x + "\t" + families.get(x).married + "\t" + families.get(x).divorce + "\t\t" + families.get(x).husb_id + "\t\t" + individuals.get(families.get(x).husb_id).name + "\t" + families.get(x).wife_id + "\t" + individuals.get(families.get(x).wife_id).name + "\t");
			families.get(x).printChildren();
			System.out.println();
		}
			
		br.close();
	}

}
