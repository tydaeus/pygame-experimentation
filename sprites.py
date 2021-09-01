import pygame, pygame.surfarray as surfarray

r = red = pygame.Color(255, 0, 0, 255)
c = clear = pygame.Color(0, 0, 0, 0)

def get_test_surface():
    testSymbolSurface = pygame.Surface((11, 11), flags=pygame.SRCALPHA)
    testSymbolPxArray = pygame.PixelArray(testSymbolSurface)

    testSymbolPxArray[:,0:1] =      [c, r, r, r, r, r, r, r, r, r, c]
    testSymbolPxArray[:,1:2] =      [r, c, c, c, c, c, c, c, c, c, r]
    testSymbolPxArray[:,2:3] =      [r, c, c, c, c, r, c, c, c, c, r]
    testSymbolPxArray[:,3:4] =      [r, c, c, c, c, c, r, c, c, c, r]
    testSymbolPxArray[:,4:5] =      [r, c, c, c, c, c, c, r, c, c, r]
    testSymbolPxArray[:,5:6] =      [r, c, r, r, r, r, r, r, r, c, r]
    testSymbolPxArray[:,6:7] =      [r, c, c, c, c, c, c, r, c, c, r]
    testSymbolPxArray[:,7:8] =      [r, c, c, c, c, c, r, c, c, c, r]
    testSymbolPxArray[:,8:9] =      [r, c, c, c, c, r, c, c, c, c, r]
    testSymbolPxArray[:,9:10] =     [r, c, c, c, c, c, c, c, c, c, r]
    testSymbolPxArray[:,10:11] =    [c, r, r, r, r, r, r, r, r, r, c]

    del testSymbolPxArray

    return testSymbolSurface
