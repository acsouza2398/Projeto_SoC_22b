#
TARGET = spider

# add 'export SOCEDS_DEST_ROOT=~/altera/14.0/embedded' in /etc/profile
# 
ALT_DEVICE_FAMILY ?= soc_cv_av

CFLAGS = -g -Wall -std=gnu++11 -D$(ALT_DEVICE_FAMILY) -I${SOCEDS_DEST_ROOT}/ip/altera/hps/altera_hps/hwlib/include -I${SOCEDS_DEST_ROOT}/ip/altera/hps/altera_hps/hwlib/include/$(ALT_DEVICE_FAMILY)/
LDFLAGS =  -g -Wall  -lstdc++ -lrt -lpthread
#CC = $(CROSS_COMPILE)gcc
CC = $(CROSS_COMPILE)g++
ARCH= arm

all: $(TARGET)

$(TARGET): Main.o CSpider.o CSpiderLeg.o CMotor.o terasic_os.o mmap.o Queue.o QueueCommand.o PIO_LED.o PIO_BUTTON.o
	$(CC) $(LDFLAGS)   $^ -o $@ 

%.o : %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

.PHONY: clean
clean:
	rm -f $(TARGET) *.a *.o *~
