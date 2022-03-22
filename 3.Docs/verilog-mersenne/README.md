# Verilog Mersenne Twister Readme

For more information and updates: http://alexforencich.com/wiki/en/verilog/mersenne/start

GitHub repository: https://github.com/alexforencich/verilog-mersenne

## Introduction

This is an implementation of the Mersenne Twister pseudorandom number
generator, written in Verilog with MyHDL testbenches.

## Documentation

The main code exists in the rtl subdirectory.  The 32 bit and 64 bit
implementations are contained entirely in the files axis_mt19937.v and
axis_mt19937_64.v, respectively.  The axis_mt19937 implements the 32-bit
mt19937ar algorithm while the axis_mt19937_64 module implements the 64-bit
mt19937-64 algorithm.  The only interface difference is the width of the AXI
stream interface.  After initialization, both cores can output data on every
clock cycle.

The AXI stream interface is a very standard parallel bus.  The data output is
carried by the tdata signal while the tvalid and tready signals perform the
handshaking.  The data on tdata is valid while tvalid is asserted, and it is
held until tready is asserted.  Data is only transferred when both tvalid and
tready are asserted.
AXIstream 接口是一种非常标准的并行总线。当tvalid和tready信号进行握手时，数据输出由tdata信号携带。当tvalid被断言时，tdata上的数据是有效的，并且它被持有直到ready被断言。只有当tvalid和ready都被断言时，数据才会被传输。




Seeding the PRNG can be done simply by placing the seed value on the seed_val
input and then providing a single cycle pulse on seed_start.  The seed
operation takes a rather long time due to the fact that the seed routine uses
a serialized multiplication for minimum resource utilization.  The module will
assert the busy output while the seed operation is running, and additional
seed_start pulses will be ignored until the seed operation completes.  A seed
operation with the default seed of 5489 will start automatically on the first
read attempt on the AXI bus if a seed operation has not yet taken place.
播种PRNG可以简单地通过在seed val输入中放置seed值，然后在seed启动时提供一个单周期脉冲来完成。种子操作需要相当长的时间，因为种子例程使用了序列化的乘法来实现最小的资源利用率。当种子操作正在运行时，模块将断言输出繁忙，而其他种子启动脉冲将被忽略，直到种子操作完成。如果种子操作还没有启动，那么默认种子操作5489将在AXI总线上第一次读取尝试时自动启动



### Source Files

    rtl/axis_mt19937.v     : 32 bit MT implementation, mt19937ar
    rtl/axis_mt19937_64.v  : 64 bit MT implementation, mt19937-64

### AXI Stream Interface Example //界面例子

two byte transfer with sink pause after each byte
//两个字节传输，每个字节后接收器暂停


              __    __    __    __    __    __    __    __    __
    clk    __/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__
                    _____ _________________
    tdata  XXXXXXXXX_D0__X_D1______________XXXXXXXXXXXXXXXXXXXXXXXX
                    _______________________
    tvalid ________/                       \_______________________
           ______________             _____             ___________
    tready               \___________/     \___________/


## Testing

Running the included testbenches requires MyHDL and Icarus Verilog.  Make sure
that myhdl.vpi is installed properly for cosimulation to work correctly.  The
testbenches can be run with a Python test runner like nose or py.test, or the
individual test scripts can be run with python directly.
//运行包含的测试台需要MyHDL和Icarus Verilog。确保我的myhdl.Vpi安装正确，协同仿真才能正常工作。测试工作台可以用Python测试运行器(如nose或py.test)运行，或者单独的测试脚本可以直接用python运行。


### Testbench Files

    tb/axis_ep.py               : MyHDL AXI Stream endpoints 
    tb/mt19937.py               : Reference Python implementation of mt19937ar
    tb/mt19937_64.py            : Reference Python implementation of mt19937-64
    tb/test_axis_mt19937.py     : MyHDL testbench for axis_mt19937 module
    tb/test_axis_mt19937.v      : Verilog toplevel file for axis_mt19937  cosimulation
    tb/test_axis_mt19937_64.py  : MyHDL testbench for axis_mt19937_64 module
    tb/test_axis_mt19937_64.v   : Verilog toplevel file for axis_mt19937_64 cosimulation
