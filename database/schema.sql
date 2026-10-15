-- ETPS research archive schema (MySQL 8+)
CREATE DATABASE IF NOT EXISTS etps_research CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE etps_research;

CREATE TABLE IF NOT EXISTS research_system (
  system_id INT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  volume VARCHAR(80) NOT NULL,
  evidence_status ENUM('ESTABLISHED','ACTIVE_RESEARCH','TOY_MODEL','SPECULATIVE','FICTION') NOT NULL,
  summary TEXT NOT NULL,
  assumptions TEXT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS equation_record (
  equation_id BIGINT AUTO_INCREMENT PRIMARY KEY,
  system_id INT NOT NULL,
  equation_latex TEXT NOT NULL,
  description TEXT NOT NULL,
  variable_definitions JSON NULL,
  units JSON NULL,
  domain_of_validity TEXT NOT NULL,
  derivation_notes TEXT NULL,
  source_doi VARCHAR(255) NULL,
  FOREIGN KEY (system_id) REFERENCES research_system(system_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS experiment_or_simulation (
  run_id BIGINT AUTO_INCREMENT PRIMARY KEY,
  system_id INT NOT NULL,
  run_type ENUM('ANALYTIC','SIMULATION','OBSERVATION','TOY_MODEL') NOT NULL,
  code_version VARCHAR(80) NULL,
  parameters JSON NOT NULL,
  result_summary JSON NULL,
  data_uri TEXT NULL,
  executed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (system_id) REFERENCES research_system(system_id)
);

CREATE TABLE IF NOT EXISTS reference_record (
  reference_id BIGINT AUTO_INCREMENT PRIMARY KEY,
  system_id INT NOT NULL,
  citation TEXT NOT NULL,
  doi VARCHAR(255) NULL,
  url TEXT NULL,
  source_type ENUM('PAPER','REVIEW','BOOK','DATASET','OFFICIAL_REPORT','OTHER') NOT NULL DEFAULT 'OTHER',
  verified BOOLEAN NOT NULL DEFAULT FALSE,
  FOREIGN KEY (system_id) REFERENCES research_system(system_id) ON DELETE CASCADE
);
