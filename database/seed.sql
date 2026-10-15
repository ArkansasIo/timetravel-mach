USE etps_research;
INSERT INTO research_system (system_id, title, volume, evidence_status, summary, assumptions) VALUES
(226,'Quantum Causal Networks','III','ACTIVE_RESEARCH','Graph and process models for causal order','Formalism and operational definition must be specified'),
(230,'Density Matrices and Purity','III','ESTABLISHED','Density operator properties and quantum-state mixedness','Finite-dimensional examples use positive trace-one operators'),
(301,'Special-Relativistic Time Dilation','IV','ESTABLISHED','Proper time along timelike worldlines','Inertial motion in flat spacetime for the baseline model'),
(302,'Gravitational Clock Rates','IV','ESTABLISHED','Static clock comparison in Schwarzschild exterior','Non-rotating spherical mass; r greater than Schwarzschild radius'),
(303,'Wormhole Time-Shift Proposal','IV','SPECULATIVE','Hypothetical time-shift proposals using traversable wormholes','No traversable wormhole has been observed'),
(304,'Closed Timelike Curves','IV','ACTIVE_RESEARCH','Causal pathologies in selected mathematical spacetimes','Mathematical existence does not establish physical realizability')
ON DUPLICATE KEY UPDATE title=VALUES(title), summary=VALUES(summary), assumptions=VALUES(assumptions);
