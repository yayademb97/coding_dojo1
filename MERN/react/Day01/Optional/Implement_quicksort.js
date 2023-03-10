function partition(arr, low, high) {
    const pivot = arr[Math.floor((low + high) / 2)];
    let i = low - 1;
    let j = high + 1;
    while (true) {
        do {
            i++;
        } while (arr[i] < pivot);
        do {
            j--;
        } while (arr[j] > pivot);
        if (i >= j) {
            return j;
        }
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
}
partition([1,2,10,11,3,8])
console.log(pivot);
// console.log(---------------------);
// function quicksort(arr, low = 0, high = arr.length - 1) {
//     if (low < high) {
//         const p = partition(arr, low, high);
//         quicksort(arr, low, p);
//         quicksort(arr, p + 1, high);
//     }
//     return arr;
// }
