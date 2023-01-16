#include <stdio.h>
#include <cuda_runtime.h>

__global__ void addKernel(int *a, int *b, int *c, int rows, int cols) {
    int i = blockIdx.y*blockDim.y + threadIdx.y;
    int j = blockIdx.x*blockDim.x + threadIdx.x;
    if (i < rows && j < cols) {
        int idx = i*cols + j;
        c[idx] = a[idx] + b[idx];
    }
}

__global__ void subtractKernel(int *a, int *b, int *c, int rows, int cols) {
    int i = blockIdx.y*blockDim.y + threadIdx.y;
    int j = blockIdx.x*blockDim.x + threadIdx.x;
    if (i < rows && j < cols) {
        int idx = i*cols + j;
        c[idx] = a[idx] - b[idx];
    }
}

__global__ void multiplyKernel(int *a, int *b, int *c, int rows, int cols) {
    int i = blockIdx.y*blockDim.y + threadIdx.y;
    int j = blockIdx.x*blockDim.x + threadIdx.x;
    if (i < rows && j < cols) {
        int idx = i*cols + j;
        int sum = 0;
        for (int k = 0; k < cols; k++) {
            sum += a[i*cols + k] * b[k*cols + j];
        }
        c[idx] = sum;
    }
}

void matrixAdd(int *a, int *b, int *c, int rows, int cols) {
    int size = rows*cols*sizeof(int);
    int *dev_a, *dev_b, *dev_c;
    cudaMalloc(&dev_a, size);
    cudaMalloc(&dev_b, size);
    cudaMalloc(&dev_c, size);
    cudaMemcpy(dev_a, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(dev_b, b, size, cudaMemcpyHostToDevice);
    dim3 dimBlock(16,16);
    dim3 dimGrid(cols/dimBlock.x,rows/dimBlock.y);
    addKernel<<<dimGrid, dimBlock>>>(dev_a, dev_b, dev_c, rows, cols);
    cudaMemcpy(c, dev_c, size, cudaMemcpyDeviceToHost);
    printf("Addition of two matrix:\n\n");
    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            printf("%d ",c[i][j]);
        }
        printf("\n");
    }
    cudaFree(dev_a);
    cudaFree(dev_b);
    cudaFree(dev_c);

}

void matrixSubtract(int *a, int *b, int *c, int rows, int cols) {
    int size = rows*col
    int *dev_a, *dev_b, *dev_c;
    cudaMalloc(&dev_a, size);
    cudaMalloc(&dev_b, size);
    cudaMalloc(&dev_c, size);
    cudaMemcpy(dev_a, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(dev_b, b, size, cudaMemcpyHostToDevice);
    dim3 dimBlock(16,16);
    dim3 dimGrid(cols/dimBlock.x,rows/dimBlock.y);
    subtractKernel<<<dimGrid, dimBlock>>>(dev_a, dev_b, dev_c, rows, cols);
    cudaMemcpy(c, dev_c, size, cudaMemcpyDeviceToHost);
    printf("\nSubtraction of two matrix:\n\n");
    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            printf("%d ",c[i][j]);
        }
        printf("\n");
    }
    cudaFree(dev_a);
    cudaFree(dev_b);
    cudaFree(dev_c);
}

void matrixMultiplication(int *a, int *b, int *c, int rows, int cols) {
    int size = rows*col
    int *dev_a, *dev_b, *dev_c;
    cudaMalloc(&dev_a, size);
    cudaMalloc(&dev_b, size);
    cudaMalloc(&dev_c, size);
    cudaMemcpy(dev_a, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(dev_b, b, size, cudaMemcpyHostToDevice);
    dim3 dimBlock(16,16);
    dim3 dimGrid(cols/dimBlock.x,rows/dimBlock.y);
    multiplyKernel<<<dimGrid, dimBlock>>>(dev_a, dev_b, dev_c, rows, cols);
    cudaMemcpy(c, dev_c, size, cudaMemcpyDeviceToHost);
    printf("\nMultiplication of two matrix:\n\n");
    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            printf("%d ",c[i][j]);
        }
        printf("\n");
    }
    cudaFree(dev_a);
    cudaFree(dev_b);
    cudaFree(dev_c);
}

int main(){

    int a[3][3]={{13,62,3},{46,25,6},{7,18,89}},
        b[3][3] ={{9,8,7},{6,5,4},{3,2,1}}, 
        c[3][3];
    int rows=3,cols=3;

matrixAdd(&a,&b,&c,rows,cols);
matrixSubtract(&a,&b,&c,rows,cols);
matrixMultiplication(&a,&b,&c,rows,cols);

    return 0;
}