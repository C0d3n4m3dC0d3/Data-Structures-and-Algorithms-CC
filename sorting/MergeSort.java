import java.util.Scanner;

class MergeSort {
    private void merge(int[] arr, int s, int m, int e) {
		int l1 = (m - s) + 1;
		int l2 = e - m;

		//temporary arrays
		int[] t1 = new int[l1];
		int[] t2 = new int[l2];

		for(int x = 0; x < l1; x++) {t1[x] = arr[s + x]; } //s - m
		for(int y = 0; y < l2; y++) {t2[y] = arr[m + 1 + y]; } //m+1 - e

		int i = 0, j = 0, k = s;

		while(i < l1 && j < l2) {
			if(t1[i] <= t2[j]) {
				arr[k] = t1[i];
				i++;
			}
			else {
				arr[k] = t2[j];
				j++;
			}
			k++;
		}

		while(i < l1) {
			arr[k] = t1[i];
			i++;
			k++;
		}
		while(j < l2) {
			arr[k] = t2[j];
			j++;
			k++;
		}
	}

	private void mergeSort(int[] arr, int s, int e) {
		if(s < e) {
			int m = (s + e) / 2;
			mergeSort(arr, s, m);
			mergeSort(arr, m+1, e);
			merge(arr, s, m, e);
		}
	}

    public static void main(String[] args) {
		Scanner ip = new Scanner(System.in);
		System.out.print("Enter array size: ");
		int n = ip.nextInt();

		int []arr = new int[n];
		System.out.format("Enter %d elements:\n", n);
		for(int i = 0; i<n; arr[i++] = ip.nextInt());

		MergeSort ms = new MergeSort();
		ms.mergeSort(arr, 0, n-1);
		System.out.println("Sorted Array:");
		for(int i = 0; i<n; System.out.print(arr[i++] + " "));
	}
}
