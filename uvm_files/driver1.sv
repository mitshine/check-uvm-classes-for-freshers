
class driver1 extends uvm_driver;

rand bit  in;

virtual function run_phase()

endfunction

virtual function void build_phase(uvm_phase phase);
  super.build_phase(phase);
  s0 = uvm_sequencer#(Item)::type_id::create("s0", this);
endfunction

endclass