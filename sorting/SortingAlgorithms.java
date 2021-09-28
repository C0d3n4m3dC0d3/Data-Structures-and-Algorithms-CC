//Sorting Algorithm Implementation in Java
//1. Bubble Sort
//2. Selection Sort
//3. Insertion Sort
//4. Merge Sort

class SortingAlgorithms{
	public void display(int [] arr, String msg){
		System.out.println(msg);
		int n = arr.length;
		for(int a: arr ){
			System.out.print(a + " ");
		}
		System.out.println();
    }

	public void swap(int[] arr, int x, int y){
		arr[x] = arr[x] + arr[y];
		arr[y] = arr[x] - arr[y];
		arr[x] = arr[x] - arr[y];
	}

	public void bubbleSort(int arr[]){
		display(arr, "Before Bubble Sort:");
		int n = arr.length;
		for(int i = n-1; i >= 0; i--){
			for(int j = 0; j<i; j++){
				if(arr[j] > arr[i]){
					swap(arr, i, j);
				}
			}
		}
		display(arr, "After Bubble Sort:");
	}

	public void selectionSort(int arr[]){
		display(arr, "Before Selection Sort:");
		int n = arr.length;
		int maxi;
		for(int i = n-1; i >= 0; i--){
			maxi = 0;
			for(int j = 0; j<=i; j++){
				if(arr[j] > arr[maxi]){
					maxi = j;
				}
			}
			if(maxi != i){
				swap(arr, maxi, i);
			}
		}
		display(arr, "After Selection Sort:");
	}

	public void insertionSort(int arr[]){
		display(arr, "Before Insertion Sort:");
		int n = arr.length;
		int temp;
		for(int i = 1; i<n; i++){
			for(int j = 0; j < i; j++){
				if(arr[j] > arr[i]){
					temp = arr[i];
					for(int k = i; k > j; k--){
						arr[k] = arr[k-1];
					}
					arr[j] = temp;
					break;
				}
			}
		}
		display(arr, "After Insertion Sort:");
	}

	public int[] merge(int[] a, int s1, int e1, int s2, int e2){
		int i = s1, j = s2, k = 0, n, m;
		System.out.println(s1 + " " + e1 + " " + s2 + " " +e2);
		if(s1 == e1)
			n = 1;
		else
			n = e1 - s1;
		if(s2 == e2)
			m = 1;
		else
			m = e2 - s2;
		int [] arr = new int[n+m];
		while(i <= e1 & j <= e2){
			System.out.println(a[s1] + " " + a[s2]);
			if(a[i] < a[j]){
				arr[k] = a[i];
				k+=1;
				i+=1;
			}
			else{
				arr[k] = a[j];
				k+=1;
				j+=1;
			}
		}
		while(i <= e1){
			arr[k] = a[i];
			k+=1;
			i+=1;
		}
		while(j <= e2){
			arr[k] = a[j];
			k+=1;
			j+=1;
		}
		display(arr, "After merging:");
		System.out.println();
		return arr;
	}

	public int[] mergeSort(int[] arr, int s, int e){
		int m, a[], b[], c[];
		if(s < e){
			m = (s+e)/2;
			a = mergeSort(arr, s, m);
			b = mergeSort(arr, m+1, e);
			merge(arr, s, m, m+1, e);
		}
		return
	}

    public static void main(String[] args){
		SortingAlgorithms sort = new SortingAlgorithms();
		int arr[] = {4, 2, 5, 1, 0, 9, 7};
		sort.bubbleSort(arr);
		arr = new int[] {4, 2, 5, 1, 0, 9, 7};
		sort.selectionSort(arr);
		arr = new int[] {4, 2, 5, 1, 0, 9, 7};
		sort.insertionSort(arr);
		arr = new int[] {4, 2, 5, 1, 0, 9, 7};
		sort.mergeSort(arr, 0, arr.length-1);
	}
}
