//know the generics in JAVA
class Node<T> {
	private T data;
	private Node next;
	public Node(T data){
		this.data = data;
		this.next = null;
	}
	
	public Node<T> getData(){
		return this.data;
	}

	public void setData(T data){
		this.data = data;
	}

	public Node<T> getNext(){
		return this.next;
	}

	public void setNext(Node<T> node){
		this.next = node;
	}

	public void print(){
		Node<T> 
	}	

	public void print(){
		Node<T> list = 
	}
}


class LinkedList<T> {
	private Node<T> head;
	
	public LinkedList(){
		head = null;
	}

	public void append(T data){
		Node<T> node = new Node(data);
		if(head == null){
			head = node;
			return;
		}
		Node<T> list = node;
		while( list.getNext() != null){
			list = list.getNext();
		}
		list.setNext(node);
	}
}

public class SinglyLinkedList{
	public static void main(String[] args){,
		LinkedList<Integer> linkedList = new LinkedList<Integer>();
		linkedList.append(3);
		linkedList.append(1);
		linkedList.append(4);
		linkedList.append(6);
		linkedList.print();
	}
}

//Write the different methods for inserting 