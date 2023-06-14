/**
 * Author: Dylan Miles
 * 4883-Software-Tools
 * A05 - Graphviz family tree generation
 */
package graphvizGen;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		List<String> clanNames = new ArrayList<>();
		File file2 = new File(new File(".").getAbsolutePath().replace(".", "") + "clan_names.txt");

		BufferedReader br2 = null;
		try {
			br2 = new BufferedReader(new FileReader(file2));
		} catch (FileNotFoundException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		String st2;
		try {
			while ((st2 = br2.readLine()) != null) {
				clanNames.add(st2);
			}
		} catch (IOException e2) {
			e2.printStackTrace();
		}
		File file = new File(new File(".").getAbsolutePath().replace(".", "") + "tree.csv");

		BufferedReader br = null;
		try {
			br = new BufferedReader(new FileReader(file));
		} catch (FileNotFoundException e1) {
			e1.printStackTrace();
		}
		String st;
		try {
			String output = "digraph familytree {\n";
			int i = 0;
			br.readLine();
			List<Person> treeList = new ArrayList<Person>();
			while ((st = br.readLine()) != null) {
				String[] s = st.split(",");
				if (s.length < 3)
					continue;
				String pid = s[0];
				String name = s[1];
				String gender = s[2];
				String generation = s[3];
				String byear = s[4];
				String dyear = s[5];
				String dage = s[6];
				String myear = s[7];
				String mage = s[8];
				String ptype = s[9];
				String randClan = clanNames.get((int) (Math.random() * clanNames.size()));
				String clan = randClan;
				String spouceid = s[11];
				String parentid1 = s[12];
				String parentid2 = s[13];
				String parentnodeid = s[14];
				Person p = new Person();
				p.pid = pid;
				p.name = name;
				p.gender = gender;
				p.generation = generation;
				p.byear = byear;
				p.dyear = dyear;
				p.dage = dage;
				p.myear = myear;
				p.mage = mage;
				p.ptype = ptype;
				p.clan = clan;
				p.spouceid = spouceid;
				p.parentid1 = parentid1;
				p.parentid2 = parentid2;
				p.parentnodeid = parentnodeid;
				treeList.add(p);

			}
			/*
			 * Make children have the same clan as their parent also make married women take
			 * the clan of their partner
			 */
			List<Person> tempList = new ArrayList<>();
			for (Person p : treeList) {
				if (p.parentid1.length() > 0) {
					try {
						p.clan = Person.getPersonById(treeList, p.parentid1).clan;
					} catch (Exception e) {
						e.printStackTrace();
					}
				} else if (p.parentid2.length() > 0) {
					p.clan = Person.getPersonById(treeList, p.parentid2).clan;

				}
				if (p.gender.equals("F") && p.spouceid.length() > 0) {
					try {
						p.clan = Person.getPersonById(treeList, p.spouceid).clan;
					} catch (Exception e) {
						e.printStackTrace();
					}

				}
				tempList.add(p);
			}
			treeList = tempList;

			/**
			 * this code is for sorting by clan
			 */
			for (String s : clanNames) {
				output += "subgraph cluster_" + s + " {\n";
				output += "label = \"" + s + " Clan\"\n";
				output += "rank=same\n";
				output += "graph[style=dotted];\n";
				output += "rankdir=TB\n";
				for (Person p : treeList) {
					if (p.clan.equals(s)) {
						String info = "[label = \"{<name> @ | <life> # | <age> & | <clan> %}\" shape = \"record\", color = \"!\"]";
						info = info.replaceAll("@", p.name);
						info = info.replaceAll("#", p.byear + "-" + p.dyear);
						int age = Integer.valueOf(p.dyear) - Integer.valueOf(p.byear);
						info = info.replaceAll("&", age + "");
						info = info.replaceAll("%", p.clan);
						info = info.replaceAll("!", p.gender.equals("M") ? "blue" : "red");
						output += p.pid + " " + info + "\n";
					}
				}
				output += "}\n";
			}
			for (Person P : treeList) {
				if (P.parentid1.length() > 0) {
					output += P.parentid1 + " -> " + P.pid + "\n";
				}
			}
			output += "}";
			Files.deleteIfExists(Paths.get(new File(".").getAbsolutePath().replace(".", "") + "output.dot"));
			Files.writeString(Paths.get(new File(".").getAbsolutePath().replace(".", "") + "output.dot"), output,
					StandardOpenOption.CREATE);

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}