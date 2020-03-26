import java.util.*;
import java.sql.*;
import java.sql.Date;


class Student {
	private String sid;
	private String sname;
	private String deptno;
	private String advisor;
	private String gen;
	private String addr;
	private String birthdate;
	private String grade;
	
	Connection connection;
	PreparedStatement query;

	public boolean setSid(String sid) {
		if(sid.equals("")||Integer.parseInt(sid)>9999||Integer.parseInt(sid)<1000) {
			return false;
		}
		this.sid = sid;
		return true;
	}

	public String getSid() {
		return sid;
	}

	public void setSname(String sname) {
		if(sname.equals("")) {
			this.sname = "null";
			return;
		}

		this.sname = sname;
	}

	public String getSname() {
		return this.sname;
	}
	

	public void setDeptno(String deptno) {
		if(deptno.equals("")) {
			this.deptno = null;
			return;
		}
		this.deptno = deptno;
	}

	public String getDeptno() {
		return deptno;
	}

	public void setAdvisor(String advisor) {
		if(advisor.equals("")) {
			this.advisor = null;
			return;
		}
		this.advisor = advisor;
	}

	public String getAdvisor() {
		return advisor;
	}

	public void setGen(String gen) {
		if(gen.equals("")) {
			this.gen = null;
			return;
		}
		this.gen = gen.toUpperCase();
	}

	public String getGen() {
		return gen;
	}

	public void setAddr(String addr) {
		if(addr.equals("")) {
			this.addr = null;
			return;
		}
		this.addr = addr;
	}

	public String getAddr() {
		return addr;
	}

	public void setBirthdate(String birthdate) {
		this.birthdate = birthdate;
	}

	public String getBirthdate() {
		return birthdate;
	}

	public void setGrade(String grade) {
		if(grade.equals("")) {
			this.grade = null;
			return;
		}
		this.grade = grade;
	}

	public String getGrade() {
		return grade;
	}
	
	public void showAll() {
		System.out.println("�й� : "+sid);
		System.out.println("�̸� : "+sname);
		System.out.println("�а� ��ȣ : "+deptno);
		System.out.println("���� ��ȣ : "+advisor);
		System.out.println("���� : "+gen);
		System.out.println("�ּ� : "+addr);
		System.out.println("���� ���� : "+birthdate);
		System.out.println("���� : "+grade);
	}
}


class SPD{
	private String sid;
	private String sname;
	private String dname;
	private String pname;
	
	public void setSid(String sid) {
		this.sid = sid;
	}
	
	public void setSname(String sname) {
		this.sname = sname;
	}
	
	public void setDname(String dname) {
		this.dname = dname;
	}
	
	public void setPname(String pname) {
		this.pname = pname;
	}
	
	public void showAll(ArrayList<SPD> spda) {
		for(int i=0;i<spda.size();i++) {
			System.out.println("�л� ��ȣ : "+spda.get(i).sid);
			System.out.println("�л� �̸� : "+spda.get(i).sname);
			System.out.println("�а� �̸� : "+spda.get(i).dname);
			System.out.println("���� �̸� : "+spda.get(i).pname);
			System.out.println();
		}
	}
}

class CRUD {

	private Connection connection;
	private PreparedStatement query;

	public void connect() {
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			connection = DriverManager.getConnection("jdbc:oracle:thin:@dbserver.yu.ac.kr:1521:XE", "student142",
					"wnsdud0415");
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	public void disconnect() {
		try {
			if (query != null)
				query.close();
			if (connection != null)
				connection.close();
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	public void create(Student s) {
		String sql = "insert into student(sid, sname, deptno, advisor, gen, addr, birthdate, grade) values(?,?,?,?,?,?, ?, ?)";
		connect();

		try {
			query = connection.prepareStatement(sql);
			query.setString(1, s.getSid());
			query.setString(2, s.getSname());
			query.setString(3, s.getDeptno());
			query.setString(4, s.getAdvisor());
			query.setString(5, s.getGen());
			query.setString(6, s.getAddr());
			query.setString(7, s.getBirthdate());
			query.setString(8, s.getGrade());
			query.executeUpdate();
		} catch (Exception e) {
			System.out.println(e);
		} finally {
			disconnect();
			System.out.println("�߰� �Ϸ�");
		}

	}

	void read(int usid) {
		String sql = "select * from student where sid = ?";
		Student s = new Student();
		connect();
		
		try {
			query = connection.prepareStatement(sql);
			query.setInt(1, usid);
			ResultSet result = query.executeQuery();
			
			while(result.next()) {
				
				s.setSid(result.getString("sid"));
				
				if(result.getString("sname")==null)
					s.setSname("");
				else
					s.setSname(result.getString("sname"));
				
				if(result.getString("deptno")==null)
					s.setDeptno("");
				else
					s.setDeptno(result.getString("deptno"));
				
				if(result.getString("advisor")==null)
					s.setAdvisor("");
				else
					s.setAdvisor(result.getString("advisor"));
				
				if(result.getString("gen")==null)
					s.setGen("");
				else
					s.setGen(result.getString("gen"));
				
				if(result.getString("addr")==null)
					s.setAddr("");
				else
					s.setAddr(result.getString("addr"));
				
				if(result.getString("birthdate")==null) 
					s.setBirthdate("null");
				else {
					String temp = result.getString("birthdate");
					temp = temp.substring(0,10);
					s.setBirthdate(temp);
				}
				if(result.getString("grade")==null)
					s.setGrade("");
				else
					s.setGrade(result.getString("grade"));
			}
			
		}catch(Exception e) {
			System.out.println(e);
		}finally {
			disconnect();
			s.showAll();
		}
	}

	void update(int usid, Student s) {
		String sql = "update student set sname = ?, deptno = ?, advisor = ?, gen = ?, addr = ?, birthdate = ?, grade = ? where sid = ?";
		connect();
		
		try {
			query = connection.prepareStatement(sql);
			query.setString(1, s.getSname());
			query.setString(2, s.getDeptno());
			query.setString(3, s.getAdvisor());
			query.setString(4, s.getGen());
			query.setString(5, s.getAddr());
			query.setString(6, s.getBirthdate());
			query.setString(7, s.getGrade());
			query.setInt(8, usid);
			query.executeUpdate();
			
		}catch(Exception e) {
			System.out.println(e);
			
		}finally {
			disconnect();
			System.out.println("���� �Ϸ�");
			
		}
	}
	
	void rdept(int rdeptno) {
		String sql = "select sid, sname, dname, pname from student s, department d, professor p where s.advisor = p.pid and s.deptno = d.deptno and s.deptno = ?";
		Student s = new Student();
		ArrayList<SPD> spda = new ArrayList<SPD>();
		SPD spd = null;
		connect();
		
		try {
			query = connection.prepareStatement(sql);
			query.setInt(1, rdeptno);
			ResultSet result = query.executeQuery();
			
			while(result.next()) {
				
				spd = new SPD();
				
				spd.setSid(result.getString("sid"));
				spd.setSname(result.getString("sname"));
				spd.setDname(result.getString("dname"));
				spd.setPname(result.getString("pname"));
				
				spda.add(spd);
		
			}
			
		}catch(Exception e) {
			System.out.println(e);
		}finally {
			disconnect();
			spd.showAll(spda);
		}
	}

	void delete(int dsid) {
		String sql = "delete from student where sid = ?";
		connect();

		try {
			query = connection.prepareStatement(sql);
			query.setInt(1, dsid);
			query.executeUpdate();
		} catch (Exception e) {
			System.out.println(e);
		} finally {
			disconnect();
			System.out.println("���� �Ϸ�");
		}
	}
}

public class JDBCTest {

	public static void main(String args[]) {

		while (true) {
			int select = 0;
			Scanner scanner = new Scanner(System.in);
			System.out.printf("Menu(1: �л� �߰�, 2: �л� ����, 3: �л� ����, 4: �л� �˻�, 5: �а� ���, 6: ����) : ");

			select = scanner.nextInt();
			scanner.nextLine();

			if (select < 1 || select > 6) {
				System.out.println("���� �Է��� �߸� �Ǿ����ϴ�.");
				continue;
			}

			if (select == 1) {
						
				Student s = new Student();
				CRUD create = new CRUD();
				
				System.out.printf("�й�(4�ڸ� ����) : ");
				if(s.setSid(scanner.nextLine())==false) {
					System.out.println("�й� ���Ŀ� ���� �ʰų� �й��� �Է����� �ʾҽ��ϴ�.");
					continue;
				}

				System.out.printf("�̸� : ");
				s.setSname(scanner.nextLine());

				System.out.printf("�а� ��ȣ : ");
				s.setDeptno(scanner.nextLine());

				System.out.printf("���� ��ȣ : ");
				s.setAdvisor(scanner.nextLine());

				System.out.printf("���� : ");
				s.setGen(scanner.nextLine());

				System.out.printf("�ּ� : ");
				s.setAddr(scanner.nextLine());

				System.out.printf("������� : ");
				s.setBirthdate(scanner.nextLine());

				System.out.printf("���� : ");
				s.setGrade(scanner.nextLine());
				
				create.create(s);

			}
			
			else if (select ==2) {
				int dsid;
				System.out.printf("������ �й� �Է� : ");
				dsid = scanner.nextInt();
				scanner.nextLine();
				
				CRUD delete = new CRUD();
				
				delete.delete(dsid);
			}
			
			else if (select == 3) {
				int usid;
				System.out.printf("������ �й� �Է� : ");
				usid = scanner.nextInt();
				scanner.nextLine();
				
				CRUD update = new CRUD();
				update.read(usid);
				
				Student s = new Student();

				System.out.printf("�̸� : ");
				s.setSname(scanner.nextLine());

				System.out.printf("�а� ��ȣ : ");
				s.setDeptno(scanner.nextLine());

				System.out.printf("���� ��ȣ : ");
				s.setAdvisor(scanner.nextLine());

				System.out.printf("���� : ");
				s.setGen(scanner.nextLine());

				System.out.printf("�ּ� : ");
				s.setAddr(scanner.nextLine());

				System.out.printf("������� : ");
				s.setBirthdate(scanner.nextLine());

				System.out.printf("���� : ");
				s.setGrade(scanner.nextLine());
				
				update.update(usid, s);
			}
			
			else if (select ==4) {
				int rsid;
				System.out.printf("�˻��� �й� �Է� : ");
				rsid = scanner.nextInt();
				scanner.nextLine();
				
				CRUD read = new CRUD();
				
				read.read(rsid);
			}
			
			else if (select ==5) {
				int rdeptno;
				System.out.println("�˻��� �а� ��ȣ �Է� : ");
				rdeptno = scanner.nextInt();
				scanner.nextLine();
				
				CRUD rdept = new CRUD();
				
				rdept.rdept(rdeptno);
			}

			else if (select == 6) {
				System.out.println("�����մϴ�.");
				break;
			}
		}

	}
}
