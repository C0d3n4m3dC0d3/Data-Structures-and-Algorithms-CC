import java.util.Scanner;

class QuickSort{
    public void swap(int [] arr, int i, int j) {
		arr[i] = arr[i] + arr[j];
		arr[j] = arr[i] - arr[j];
		arr[i] = arr[i] - arr[j];
    }

    private void hoarePartition(int[] arr, int s, int e) {
		if(s >= e) {
			return;
		}
		int pivot = arr[s];
		int i = s+1;
		int j = e;
		while(i<=j) {
		    while( (i <= j) && (arr[i] <= pivot) ) { i++; }
		    while( (i <= j) && (arr[j] > pivot) ) { j--; }
		    if(i < j) { swap(arr, i, j); }
	 	}
		if(s < j) {
		    swap(arr, s, j);
		    hoarePartition(arr, s, j-1);
		} else {
		    hoarePartition(arr, j+1, e);
	    }
	}

	private void lomutoPartition(int[] arr, int s, int e) {
		if(s >= e) {
			return;
		}
		int pivot = arr[s];
		int i = s;
		for(int j = i+1; j<=e; j++){
			if(arr[j] <= pivot) {
				i++;
				swap(arr, i, j);
			}
		}
		if( i > s) {
			swap(arr, i, s);
			lomutoPartition(arr, s, i-1);
		}
		lomutoPartition(arr, i+1, e);
	}

	public void display(String mssg, int []arr){
		System.out.println(mssg);
		for(int i : arr){
			System.out.print(" " + i);
		}
		System.out.println();
	}

    public static void main(String[] args){
	Scanner ip = new Scanner(System.in);
	int n;
	System.out.print("Enter array size: ");
	n = ip.nextInt();

	//Accepting Input
	int []arr_h = new int[n];
	int []arr_l = new int[n];
	System.out.println("Enter elements:");
	for(int i = 0; i<n; i++) {
		arr_h[i] = ip.nextInt();
		arr_l[i] = arr_h[i];
	}
	QuickSort q = new QuickSort();

	//Display Array before sorting
	q.display("Before Hoare Partitioned Quick Sort:", arr_h);

	//Perform Quick Sort with Hoare Partitioning
	q.hoarePartition(arr_h, 0, n-1);

	//Display Array after sorting
	q.display("After Hoare Partitioned Quick Sort:", arr_h);

	//Display Array before sorting
	q.display("Before Lomuto Partitioned Quick Sort:", arr_l);

	//Perform Quick Sort with Lomuto partitioning
	q.lomutoPartition(arr_l, 0, n-1);

	//Display Array after sorting
	q.display("After Lomuto Partitioned Quick Sort:", arr_l);
 }
}
