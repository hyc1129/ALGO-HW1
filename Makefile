CXX = g++
CXXFLAGS = -O2 -std=c++17 -Wall -Wextra
SRC_DIR = src
SRCS = $(wildcard $(SRC_DIR)/*.cpp)
TARGET = sortbench

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) -o $@ $^

clean:
	rm -f $(TARGET) sortbench.exe *.csv

