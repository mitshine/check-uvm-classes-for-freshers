
class driver1 extends uvm_driver;

rand bit  in;

p_sequencer sqr1;
m_sequencer sqr2;

virtual function void build_phase(uvm_phase phase);
  super.build_phase(phase);
  s0 = uvm_sequencer#(Item)::type_id::create("s0", this);
endfunction

virtual function run_phase1();
  phase.raise_objection();
  call_randomize(txn);
  phase.drop_objection();
endfuntion

virtual function run_phase();
  start_item();
  assert.randomize(txn);
  finish_item();
endfuntion

virtual task task_name();

endtask

endclass