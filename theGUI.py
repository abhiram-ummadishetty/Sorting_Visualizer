import pygame
import random

win_width = 720
win_height = 480
def show(arr,arr_len,sorted_idx):
    # loop to iterate each item of list
    for i in range(len(arr)):
        # drawing each bar with respective gap
        color = (255, 255, 255) if i <= arr_len - sorted_idx-2 else (0, 255, 0)
        pygame.draw.rect(win, color, (i * (win_width / arr_len),
                                      win_height - arr[i], win_width / arr_len, arr[i]))


def selectionsort(arr,arr_len):
    for sorted_idx in range(arr_len):
        min_idx = sorted_idx
        j = sorted_idx
        while(j!=arr_len):
            if arr[j]<arr[min_idx]:
                min_idx = j
            j+=1
        if min_idx!=sorted_idx:
            arr[sorted_idx],arr[min_idx]= arr[min_idx],arr[sorted_idx]
        delay = 50
        win.fill((0, 0, 0))
        show(arr, arr_len, sorted_idx)
        pygame.display.update()
        pygame.time.wait(delay)


def bubblesort(arr,arr_len):
    swapped = False
    for sorted_idx in range(arr_len):
        for j in range(1,arr_len-sorted_idx):
            if arr[j]<arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                swapped = True
            delay = 100
            win.fill((0, 0, 0))
            show(arr,arr_len,sorted_idx)

            # create a time delay
            pygame.time.delay(50)

            # update the display
            pygame.display.update()
            pygame.time.wait(delay)




#set up the window
win_width = 720
win_height = 480
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Selection Sort Visualizer")
win.fill((0,0,0))

#random array initialization
array_length = 50
array = [random.randint(0,win_height) for i in range(array_length)]

selectionsort(array,array_length)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit PyGame
pygame.quit()



