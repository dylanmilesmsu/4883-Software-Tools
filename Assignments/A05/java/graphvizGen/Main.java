package vizgraph;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 File file = new File("/home/bfce/eclipse-workspace/vizgraph/src/vizgraph/werg.csv");
		 
		        // Note:  Double backquote is to avoid compiler
		        // interpret words
		        // like \test as \t (ie. as a escape sequence)
		 
		        // Creating an object of BufferedReader class
		        BufferedReader br = null;
				try {
					br = new BufferedReader(new FileReader(file));
				} catch (FileNotFoundException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
		 
		        // Declaring a string variable
		        String st;
		        // Condition holds true till
		        // there is character in a string
		        
		        try {
		        	String output = "digraph familytree {\n";
		        	int i = 0;
		        	br.readLine();
		        	List<Person> treeList = new ArrayList<Person>();
					while ((st = br.readLine()) != null) {
						if(st.length() < 3)
							continue;
						String[] s = st.split(",");
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
						String clan = s[10];
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
//						System.out.println(generation);
						
					    // Print the string
//					    System.out.println(st);
					    i++;
					    if(i > 100) {
					    	break;
					    }
					    
					}
					int lastGen = 0;
					for(Person P : treeList) {
						int generation = Integer.valueOf(P.generation);
						if(lastGen < generation) {
							lastGen = generation;
						}
					}
					for(int gen = 0; gen <= lastGen; gen++) {
						output += "subgraph cluster_" + gen + " {\n";
						output += "label = \" Generation " + gen + "\"\n";
						output += "rank=same\n";
						output += "graph[style=dotted];\n";
						output += "rankdir=LR\n";
						for(Person p : treeList) {
							if(Integer.valueOf(p.generation) == gen) {
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
//						output += "cluster_" + (gen-1) + " -> " + " cluster_" + gen + "\n";
					}
					for(Person P : treeList) {
						if(P.parentid1.length() > 0) {
							output += P.parentid1 + " -> " + P.pid + "\n";
						}
					}
					output += "}";
					System.out.println(output);
					
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	}

}
