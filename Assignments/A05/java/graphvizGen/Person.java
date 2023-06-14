<<<<<<< HEAD
package graphvizGen;

import java.util.List;

public class Person {
    String pid;
    String name;
    String gender;
    String generation;
    String byear;
    String dyear;
    String dage;
    String myear;
    String mage;
    String ptype;
    String clan;
    String spouceid;
    String parentid1;
    String parentid2;
    String parentnodeid;

    public static Person getPersonById(List<Person> person, String id) {
        for(Person p : person) {
            if(p.pid.equals(id))
                return p;
        }
        return null;
    }
}
=======
package vizgraph;

public class Person {
	String pid;
	String name;
	String gender;
	String generation;
	String byear;
	String dyear;
	String dage;
	String myear;
	String mage;
	String ptype;
	String clan;
	String spouceid;
	String parentid1;
	String parentid2;
	String parentnodeid;
}
>>>>>>> e8178c2e10153f1620fffca073167d35bb0c3792
