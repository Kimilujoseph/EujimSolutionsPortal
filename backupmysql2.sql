-- MySQL dump 10.13  Distrib 8.0.42, for Linux (x86_64)
--
-- Host: localhost    Database: eujim_production
-- ------------------------------------------------------
-- Server version	8.0.42-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add job seeker',6,'add_jobseeker'),(22,'Can change job seeker',6,'change_jobseeker'),(23,'Can delete job seeker',6,'delete_jobseeker'),(24,'Can view job seeker',6,'view_jobseeker'),(25,'Can add job seeker certification',7,'add_jobseekercertification'),(26,'Can change job seeker certification',7,'change_jobseekercertification'),(27,'Can delete job seeker certification',7,'delete_jobseekercertification'),(28,'Can view job seeker certification',7,'view_jobseekercertification'),(29,'Can add education',8,'add_education'),(30,'Can change education',8,'change_education'),(31,'Can delete education',8,'delete_education'),(32,'Can view education',8,'view_education'),(33,'Can add skill',9,'add_skill'),(34,'Can change skill',9,'change_skill'),(35,'Can delete skill',9,'delete_skill'),(36,'Can view skill',9,'view_skill'),(37,'Can add skill set',10,'add_skillset'),(38,'Can change skill set',10,'change_skillset'),(39,'Can delete skill set',10,'delete_skillset'),(40,'Can view skill set',10,'view_skillset'),(41,'Can add job posting',11,'add_jobposting'),(42,'Can change job posting',11,'change_jobposting'),(43,'Can delete job posting',11,'delete_jobposting'),(44,'Can view job posting',11,'view_jobposting'),(45,'Can add job posting skill',12,'add_jobpostingskill'),(46,'Can change job posting skill',12,'change_jobpostingskill'),(47,'Can delete job posting skill',12,'delete_jobpostingskill'),(48,'Can view job posting skill',12,'view_jobpostingskill'),(49,'Can add user',13,'add_user'),(50,'Can change user',13,'change_user'),(51,'Can delete user',13,'delete_user'),(52,'Can view user',13,'view_user'),(53,'Can add session',14,'add_session'),(54,'Can change session',14,'change_session'),(55,'Can delete session',14,'delete_session'),(56,'Can view session',14,'view_session'),(57,'Can add recruiter',15,'add_recruiter'),(58,'Can change recruiter',15,'change_recruiter'),(59,'Can delete recruiter',15,'delete_recruiter'),(60,'Can view recruiter',15,'view_recruiter'),(61,'Can add recruiter tracking',16,'add_recruitertracking'),(62,'Can change recruiter tracking',16,'change_recruitertracking'),(63,'Can delete recruiter tracking',16,'delete_recruitertracking'),(64,'Can view recruiter tracking',16,'view_recruitertracking'),(65,'Can add recruiter doc',17,'add_recruiterdoc'),(66,'Can change recruiter doc',17,'change_recruiterdoc'),(67,'Can delete recruiter doc',17,'delete_recruiterdoc'),(68,'Can view recruiter doc',17,'view_recruiterdoc'),(69,'Can add job listing',18,'add_joblisting'),(70,'Can change job listing',18,'change_joblisting'),(71,'Can delete job listing',18,'delete_joblisting'),(72,'Can view job listing',18,'view_joblisting');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'job_posting','jobposting'),(12,'job_posting','jobpostingskill'),(18,'job_scraper','joblisting'),(8,'jobseeker','education'),(6,'jobseeker','jobseeker'),(7,'jobseeker','jobseekercertification'),(15,'recruiter','recruiter'),(17,'recruiter','recruiterdoc'),(16,'recruiter','recruitertracking'),(14,'sessions','session'),(9,'skills','skill'),(10,'skills','skillset'),(13,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-07-28 11:18:22.618694'),(2,'auth','0001_initial','2025-07-28 11:19:33.624239'),(3,'admin','0001_initial','2025-07-28 11:19:48.892949'),(4,'admin','0002_logentry_remove_auto_add','2025-07-28 11:19:49.110516'),(5,'admin','0003_logentry_add_action_flag_choices','2025-07-28 11:19:49.642630'),(6,'contenttypes','0002_remove_content_type_name','2025-07-28 11:19:58.982612'),(7,'auth','0002_alter_permission_name_max_length','2025-07-28 11:20:09.229307'),(8,'auth','0003_alter_user_email_max_length','2025-07-28 11:20:11.305118'),(9,'auth','0004_alter_user_username_opts','2025-07-28 11:20:12.541822'),(10,'auth','0005_alter_user_last_login_null','2025-07-28 11:20:16.678809'),(11,'auth','0006_require_contenttypes_0002','2025-07-28 11:20:16.948866'),(12,'auth','0007_alter_validators_add_error_messages','2025-07-28 11:20:17.220245'),(13,'auth','0008_alter_user_username_max_length','2025-07-28 11:20:24.747250'),(14,'auth','0009_alter_user_last_name_max_length','2025-07-28 11:20:32.399224'),(15,'auth','0010_alter_group_name_max_length','2025-07-28 11:20:33.555851'),(16,'auth','0011_update_proxy_permissions','2025-07-28 11:20:33.941696'),(17,'auth','0012_alter_user_first_name_max_length','2025-07-28 11:20:41.956356'),(18,'skills','0001_initial','2025-07-28 11:20:50.959214'),(21,'users','0001_initial','2025-07-28 11:32:42.896912'),(25,'job_scraper','0001_initial','2025-07-28 11:45:26.087549'),(27,'sessions','0001_initial','2025-07-28 11:45:34.604516'),(28,'skills','0002_initial','2025-07-28 11:45:37.726420'),(30,'jobseeker','0001_initial','2025-07-28 12:06:42.011686'),(31,'job_posting','0001_initial','2025-07-28 12:19:56.865917'),(32,'recruiter','0001_initial','2025-07-28 12:19:57.039099'),(33,'job_posting','0002_initial','2025-07-28 12:19:57.173855'),(34,'recruiter','0002_initial','2025-07-28 12:19:57.285152'),(35,'users','0002_user_deleted_by','2025-07-28 14:19:43.300942'),(36,'jobseeker','0002_jobseeker_user_alter_jobseeker_location','2025-07-29 12:33:28.080747'),(37,'jobseeker','0003_alter_education_user_and_more','2025-07-29 13:44:46.524746'),(38,'jobseeker','0004_remove_jobseekercertification_createdat_and_more','2025-07-29 14:18:38.012373'),(39,'jobseeker','0005_rename_created_at_jobseekercertification_createdat_and_more','2025-07-29 14:23:21.831602');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `education_qualifications`
--

DROP TABLE IF EXISTS `education_qualifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `education_qualifications` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `institution_name` varchar(100) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `degree` varchar(20) NOT NULL,
  `field_of_study` varchar(100) NOT NULL,
  `start_year` int unsigned NOT NULL,
  `end_year` int unsigned DEFAULT NULL,
  `is_current` tinyint(1) NOT NULL,
  `description` longtext,
  `school_logo` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `education_qualifications_user_id_b490924d_fk_users_id` (`user_id`),
  CONSTRAINT `education_qualifications_user_id_b490924d_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `education_qualifications_chk_1` CHECK ((`start_year` >= 0)),
  CONSTRAINT `education_qualifications_chk_2` CHECK ((`end_year` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `education_qualifications`
--

LOCK TABLES `education_qualifications` WRITE;
/*!40000 ALTER TABLE `education_qualifications` DISABLE KEYS */;
INSERT INTO `education_qualifications` VALUES (3,'Kenyatta University','Bachelor of Science','bachelor','Computer Science',2022,NULL,1,'A four-year undergraduate program covering fundamental concepts in programming, algorithms, data structures, software engineering, and computer systems.',NULL,'2025-07-29 14:08:07.213511','2025-07-29 14:08:07.213602',2),(4,'Egerton University','Master of Business Administration','master','Business Administration',2025,NULL,1,'A two-year graduate program focusing on advanced business strategies, leadership, finance, marketing, and organizational management.',NULL,'2025-07-29 14:09:15.677741','2025-07-29 14:09:15.677814',2),(5,'Moi University','DIploma','diploma','Digital Marketing',2022,2023,0,'\"A one-year specialized program teaching SEO, social media marketing, content strategy, PPC advertising, and analytics tools',NULL,'2025-07-29 14:12:41.692474','2025-07-29 14:12:41.692568',2);
/*!40000 ALTER TABLE `education_qualifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_posting_skills`
--

DROP TABLE IF EXISTS `job_posting_skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_posting_skills` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `job_posting_id` bigint NOT NULL,
  `skill_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `job_posting_skills_job_posting_id_skill_id_c2f216be_uniq` (`job_posting_id`,`skill_id`),
  KEY `job_posting_skills_skill_id_12f8083f_fk_skills_id` (`skill_id`),
  CONSTRAINT `job_posting_skills_job_posting_id_4152e8c1_fk_job_postings_id` FOREIGN KEY (`job_posting_id`) REFERENCES `job_postings` (`id`),
  CONSTRAINT `job_posting_skills_skill_id_12f8083f_fk_skills_id` FOREIGN KEY (`skill_id`) REFERENCES `skills` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_posting_skills`
--

LOCK TABLES `job_posting_skills` WRITE;
/*!40000 ALTER TABLE `job_posting_skills` DISABLE KEYS */;
INSERT INTO `job_posting_skills` VALUES (1,1,2);
/*!40000 ALTER TABLE `job_posting_skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_postings`
--

DROP TABLE IF EXISTS `job_postings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_postings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `requirements` longtext NOT NULL,
  `responsibilities` longtext NOT NULL,
  `location` varchar(100) NOT NULL,
  `job_type` varchar(20) NOT NULL,
  `experience_level` varchar(20) NOT NULL,
  `salary_range_min` decimal(10,2) DEFAULT NULL,
  `salary_range_max` decimal(10,2) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `posted_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `application_deadline` date DEFAULT NULL,
  `views_count` int unsigned NOT NULL,
  `applications_count` int unsigned NOT NULL,
  `recruiter_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `job_postings_recruiter_id_d3a2cfbf` (`recruiter_id`),
  CONSTRAINT `job_postings_chk_1` CHECK ((`views_count` >= 0)),
  CONSTRAINT `job_postings_chk_2` CHECK ((`applications_count` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_postings`
--

LOCK TABLES `job_postings` WRITE;
/*!40000 ALTER TABLE `job_postings` DISABLE KEYS */;
INSERT INTO `job_postings` VALUES (1,'Full stack developer','Lead daily operations for flagship retail location in downtown area. Bonus potential based on store performance.','3+ years retail management experience, proven track record of meeting sales goals, availability for nights/weekends.','Manage team of 15 associates, oversee inventory and merchandising, ensure excellent customer service, analyze sales reports','Nairobi,Kenya','part_time','entry',50000.00,150000.00,1,'2025-07-30 14:25:08.290690','2025-07-31 11:52:45.295135','2025-07-28',6,0,1);
/*!40000 ALTER TABLE `job_postings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_scraper_joblisting`
--

DROP TABLE IF EXISTS `job_scraper_joblisting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_scraper_joblisting` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `company` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `url` varchar(200) NOT NULL,
  `source` varchar(20) NOT NULL,
  `job_type` varchar(100) DEFAULT NULL,
  `posted_at` datetime(6) DEFAULT NULL,
  `scraped_at` datetime(6) NOT NULL,
  `description` longtext,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`),
  KEY `job_scraper_source_55964a_idx` (`source`),
  KEY `job_scraper_title_aa5a3c_idx` (`title`),
  KEY `job_scraper_company_c9a117_idx` (`company`)
) ENGINE=InnoDB AUTO_INCREMENT=265 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_scraper_joblisting`
--

LOCK TABLES `job_scraper_joblisting` WRITE;
/*!40000 ALTER TABLE `job_scraper_joblisting` DISABLE KEYS */;
INSERT INTO `job_scraper_joblisting` VALUES (1,'Configuration Engineer','Cebu Pacific Air','Nzalae/ Nzawa locations, Kitui County, Kenya','https://ke.linkedin.com/jobs/view/configuration-engineer-at-cebu-pacific-air-4250278188','LINKEDIN','Kenya','2025-07-31 10:41:26.352206','2025-07-31 10:41:26.352220',NULL,1),(2,'Web Developer','Pinch Africa','Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/web-developer-at-pinch-africa-4268085548','LINKEDIN','Kenya','2025-07-31 10:41:29.684867','2025-07-31 10:41:29.684881',NULL,1),(3,'Backend Engineer','KenyaMOJA.com','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/backend-engineer-at-kenyamoja-com-4273868826','LINKEDIN','Kenya','2025-07-31 10:40:31.764304','2025-07-31 10:40:31.764319',NULL,1),(4,'Full Stack Engineer','KenyaMOJA.com','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/full-stack-engineer-at-kenyamoja-com-4273870306','LINKEDIN','Kenya','2025-07-31 10:21:16.688590','2025-07-31 10:21:16.688604',NULL,1),(5,'Software Engineer','Wave Mobile Money','Kenya','https://ke.linkedin.com/jobs/view/software-engineer-at-wave-mobile-money-4258795131','LINKEDIN','Kenya','2025-07-31 10:41:32.555723','2025-07-31 10:41:32.555737',NULL,1),(6,'Internship Opportunity: Microsoft Power Apps Developer','M365Connect','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/internship-opportunity-microsoft-power-apps-developer-at-m365connect-4272742467','LINKEDIN','Kenya','2025-07-31 10:41:28.065015','2025-07-31 10:41:28.065030',NULL,1),(7,'Full Stack Engineer','Techihub Inc','Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/full-stack-engineer-at-techihub-inc-3980100269','LINKEDIN','Kenya','2025-07-31 10:41:34.454666','2025-07-31 10:41:34.454680',NULL,1),(8,'Software Quality Assurance Engineer','Living Goods','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/software-quality-assurance-engineer-at-living-goods-4274336309','LINKEDIN','Kenya','2025-07-31 10:41:31.223443','2025-07-31 10:41:31.223458',NULL,1),(9,'Winjit Technologies - ESB Developer - IT Infrastructure','Winjit Technologies Pvt Ltd','Kenya','https://ke.linkedin.com/jobs/view/winjit-technologies-esb-developer-it-infrastructure-at-winjit-technologies-pvt-ltd-4275017586','LINKEDIN','Kenya','2025-07-31 10:41:33.659644','2025-07-31 10:41:33.659658',NULL,1),(10,'Senior Engineer','KenyaMOJA.com','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/senior-engineer-at-kenyamoja-com-4273870303','LINKEDIN','Kenya','2025-07-31 10:41:30.211487','2025-07-31 10:41:30.211502',NULL,1),(11,'Webmaster','KenyaMOJA.com','Kenya','https://ke.linkedin.com/jobs/view/webmaster-at-kenyamoja-com-4273873084','LINKEDIN','Kenya','2025-07-31 10:21:19.824263','2025-07-31 10:21:19.824278',NULL,1),(12,'DevOps Engineer','Living Goods','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/devops-engineer-at-living-goods-4274094286','LINKEDIN','Kenya','2025-07-31 10:41:30.822097','2025-07-31 10:41:30.822111',NULL,1),(13,'Full Stack Engineer, LearnWith.AI (Remote) - $200,000/year USD','Trilogy','Kenya','https://ke.linkedin.com/jobs/view/full-stack-engineer-learnwith-ai-remote-%24200-000-year-usd-at-trilogy-4274012830','LINKEDIN','Kenya','2025-07-31 10:41:34.891097','2025-07-31 10:41:34.891110',NULL,1),(14,'Senior Quality Analyst with Automation','Sportserve','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/senior-quality-analyst-with-automation-at-sportserve-4276982374','LINKEDIN','Kenya','2025-07-31 10:41:30.489967','2025-07-31 10:41:30.489982',NULL,1),(15,'Specialist Data Engineer (KE)','Absa Group','Kenya','https://ke.linkedin.com/jobs/view/specialist-data-engineer-ke-at-absa-group-4273860475','LINKEDIN','Kenya','2025-07-31 10:41:26.689649','2025-07-31 10:41:26.689663',NULL,1),(16,'Lead Software Engineer','Scanline VFX','Nzalae/ Nzawa locations, Kitui County, Kenya','https://ke.linkedin.com/jobs/view/lead-software-engineer-at-scanline-vfx-4250634747','LINKEDIN','Kenya','2025-07-31 10:41:33.199201','2025-07-31 10:41:33.199216',NULL,1),(17,'Senior Software Engineer','Prodapt','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/senior-software-engineer-at-prodapt-4275730733','LINKEDIN','Kenya','2025-07-31 10:41:34.735625','2025-07-31 10:41:34.735639',NULL,1),(18,'Senior Linux System Engineer (L3)','ServerHub','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/senior-linux-system-engineer-l3-at-serverhub-4277287949','LINKEDIN','Kenya','2025-07-31 10:41:32.114962','2025-07-31 10:41:32.114977',NULL,1),(19,'Senior Growth Hacking Specialist','Pepeta','Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/senior-growth-hacking-specialist-at-pepeta-4270184658','LINKEDIN','Kenya','2025-07-31 10:41:28.588505','2025-07-31 10:41:28.588520',NULL,1),(20,'Lead Python Software Engineer, Commercial Systems','Canonical','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/lead-python-software-engineer-commercial-systems-at-canonical-4277897268','LINKEDIN','Kenya','2025-07-31 10:41:29.900751','2025-07-31 10:41:29.900766',NULL,1),(21,'Senior Pipeline Developer','Scanline VFX','Nzalae/ Nzawa locations, Kitui County, Kenya','https://ke.linkedin.com/jobs/view/senior-pipeline-developer-at-scanline-vfx-4250632946','LINKEDIN','Kenya','2025-07-31 10:41:32.956081','2025-07-31 10:41:32.956095',NULL,1),(22,'Ensemble Cache Developer (Remote Opportunity)','VetsEZ','Nzalae/ Nzawa locations, Kitui County, Kenya','https://ke.linkedin.com/jobs/view/ensemble-cache-developer-remote-opportunity-at-vetsez-4275632901','LINKEDIN','Kenya','2025-07-31 10:41:31.577860','2025-07-31 10:41:31.577873',NULL,1),(23,'Senior Engineer – SailPoint IdentityNow','Redington Middle East and Africa','Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/senior-engineer-%E2%80%93-sailpoint-identitynow-at-redington-middle-east-and-africa-4272878753','LINKEDIN','Kenya','2025-07-31 10:41:31.877392','2025-07-31 10:41:31.877406',NULL,1),(24,'Senior AI Engineer, LearnWith.AI (Remote) - $200,000/year USD','Trilogy','Kenya','https://ke.linkedin.com/jobs/view/senior-ai-engineer-learnwith-ai-remote-%24200-000-year-usd-at-trilogy-4274014754','LINKEDIN','Kenya','2025-07-31 10:41:33.457338','2025-07-31 10:41:33.457352',NULL,1),(25,'Senior AI Engineer, LearnWith.AI (Remote) - $200,000/year USD','Trilogy','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/senior-ai-engineer-learnwith-ai-remote-%24200-000-year-usd-at-trilogy-4274016605','LINKEDIN','Kenya','2025-07-31 10:41:34.146124','2025-07-31 10:41:34.146140',NULL,1),(26,'Retail Store Manager','Majid Al Futtaim','Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/retail-store-manager-at-majid-al-futtaim-4272142537','LINKEDIN','Kenya','2025-07-31 10:41:07.143196','2025-07-31 10:41:07.143210',NULL,1),(27,'General Trade and BtoC Developer','Lesaffre','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/general-trade-and-btoc-developer-at-lesaffre-4277225681','LINKEDIN','Kenya','2025-07-31 10:41:08.132088','2025-07-31 10:41:08.132103',NULL,1),(28,'Graduate Sales Development Representative','Canonical','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/graduate-sales-development-representative-at-canonical-4278517768','LINKEDIN','Kenya','2025-07-31 10:41:08.941765','2025-07-31 10:41:08.941780',NULL,1),(29,'CALL FOR APPLICATIONS: BUSINESS DEVELOPMENT SERVICE PROVIDERS','ReliefWeb','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/call-for-applications-business-development-service-providers-at-reliefweb-4278012990','LINKEDIN','Kenya','2025-07-31 10:41:09.341565','2025-07-31 10:41:09.341580',NULL,1),(30,'Finance Analyst','Vistry Group','London Central, Nakuru, Kenya','https://ke.linkedin.com/jobs/view/finance-analyst-at-vistry-group-4260611885','LINKEDIN','Kenya','2025-07-31 10:41:09.985680','2025-07-31 10:41:09.985694',NULL,1),(31,'Trade Developer','KenyaMOJA.com','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/trade-developer-at-kenyamoja-com-4273865896','LINKEDIN','Kenya','2025-07-31 10:41:10.654612','2025-07-31 10:41:10.654626',NULL,1),(32,'Business Intelligence Analyst Intern','SENRI Ltd.','Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/business-intelligence-analyst-intern-at-senri-ltd-4273529269','LINKEDIN','Kenya','2025-07-31 10:41:24.571796','2025-07-31 10:41:24.571811',NULL,1),(33,'UX Designer - Developer experience','Canonical','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/ux-designer-developer-experience-at-canonical-4277438159','LINKEDIN','Kenya','2025-07-31 10:41:12.875169','2025-07-31 10:41:12.875182',NULL,1),(34,'Senior Carbon Technical Manager','BURN','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/senior-carbon-technical-manager-at-burn-4277620800','LINKEDIN','Kenya','2025-07-31 10:41:14.498386','2025-07-31 10:41:14.498401',NULL,1),(35,'UI/UX Designer','PGLS','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/ui-ux-designer-at-pgls-4275363074','LINKEDIN','Kenya','2025-07-31 10:41:14.821046','2025-07-31 10:41:14.821061',NULL,1),(36,'Senior Data Analyst, People','Wave Mobile Money','Kenya','https://ke.linkedin.com/jobs/view/senior-data-analyst-people-at-wave-mobile-money-4278333492','LINKEDIN','Kenya','2025-07-31 10:41:24.238817','2025-07-31 10:41:24.238832',NULL,1),(37,'Data Modeler','Prospect 33','Kenya','https://ke.linkedin.com/jobs/view/data-modeler-at-prospect-33-4271728999','LINKEDIN','Kenya','2025-07-31 10:41:24.861973','2025-07-31 10:41:24.861988',NULL,1),(38,'Business Systems Analyst.','Penda Health','Kenya','https://ke.linkedin.com/jobs/view/business-systems-analyst-at-penda-health-4275602351','LINKEDIN','Kenya','2025-07-31 10:41:25.241560','2025-07-31 10:41:25.241575',NULL,1),(39,'Product Analyst – Go-to-Market Strategy & Insights','PGLS','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/product-analyst-%E2%80%93-go-to-market-strategy-insights-at-pgls-4275358562','LINKEDIN','Kenya','2025-07-31 10:41:25.796904','2025-07-31 10:41:25.796918',NULL,1),(40,'Data Scientist','ENGIE Energy Access (Africa)','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/data-scientist-at-engie-energy-access-africa-4264209005','LINKEDIN','Kenya','2025-07-31 10:41:25.985229','2025-07-31 10:41:25.985243',NULL,1),(41,'Senior Business Analyst - Loans Data','Prospect 33','Kenya','https://ke.linkedin.com/jobs/view/senior-business-analyst-loans-data-at-prospect-33-4272136906','LINKEDIN','Kenya','2025-07-31 10:41:26.961024','2025-07-31 10:41:26.961039',NULL,1),(42,'Business Development Analyst','Kaleidofin Private Limited','Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/business-development-analyst-at-kaleidofin-private-limited-4277496229','LINKEDIN','Kenya','2025-07-31 10:41:27.110490','2025-07-31 10:41:27.110504',NULL,1),(43,'Senior Associate - Credit Analyst, Asset Finance','I&M Bank Uganda','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/senior-associate-credit-analyst-asset-finance-at-i-m-bank-uganda-4275341380','LINKEDIN','Kenya','2025-07-31 10:41:27.298337','2025-07-31 10:41:27.298351',NULL,1),(44,'OSINT Analyst','PGLS','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/osint-analyst-at-pgls-4275361123','LINKEDIN','Kenya','2025-07-31 10:41:27.666076','2025-07-31 10:41:27.666089',NULL,1),(45,'Business Analyst - Fraud Prevention MEA','Vyntra Global','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/business-analyst-fraud-prevention-mea-at-vyntra-global-4273598266','LINKEDIN','Kenya','2025-07-31 10:41:28.340116','2025-07-31 10:41:28.340130',NULL,1),(46,'Product Analyst - Platform & Feature Development','PGLS','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/product-analyst-platform-feature-development-at-pgls-4275363072','LINKEDIN','Kenya','2025-07-31 10:41:28.746175','2025-07-31 10:41:28.746190',NULL,1),(47,'IT Helpdesk Support','SKIMS','Los Angeles, CA','https://www.linkedin.com/jobs/view/it-helpdesk-support-at-skims-4278503672','LINKEDIN','Remote','2025-07-31 10:41:42.153530','2025-07-31 10:41:42.153545',NULL,1),(48,'IT Help Desk Tier I/II','NAMI San Diego','San Diego, CA','https://www.linkedin.com/jobs/view/it-help-desk-tier-i-ii-at-nami-san-diego-4278506043','LINKEDIN','Remote','2025-07-31 10:41:42.654973','2025-07-31 10:41:42.654988',NULL,1),(49,'IT Support Assistant','UBT','Doncaster, England, United Kingdom','https://uk.linkedin.com/jobs/view/it-support-assistant-at-ubt-4277622697','LINKEDIN','Remote','2025-07-31 10:41:43.072124','2025-07-31 10:41:43.072138',NULL,1),(50,'IT Helpdesk Support','SKIMS','Los Angeles Metropolitan Area','https://www.linkedin.com/jobs/view/it-helpdesk-support-at-skims-4278508839','LINKEDIN','Remote','2025-07-31 10:41:43.859338','2025-07-31 10:41:43.859353',NULL,1),(51,'IT Support Specialist','Framebridge','Henderson, NV','https://www.linkedin.com/jobs/view/it-support-specialist-at-framebridge-4278396171','LINKEDIN','Remote','2025-07-31 10:41:44.151799','2025-07-31 10:41:44.151814',NULL,1),(52,'IT Support Technician','Proactive Technology Management','Birmingham, AL','https://www.linkedin.com/jobs/view/it-support-technician-at-proactive-technology-management-4278339210','LINKEDIN','Remote','2025-07-31 10:41:44.650736','2025-07-31 10:41:44.650750',NULL,1),(53,'IT Specialist','The European House-Ambrosetti','Milan, Lombardy, Italy','https://it.linkedin.com/jobs/view/it-specialist-at-the-european-house-ambrosetti-4275759055','LINKEDIN','Remote','2025-07-31 10:41:45.256838','2025-07-31 10:41:45.256852',NULL,1),(54,'Help Desk IT Analyst I','City of Mesa','Mesa, AZ','https://www.linkedin.com/jobs/view/help-desk-it-analyst-i-at-city-of-mesa-4270324132','LINKEDIN','Remote','2025-07-31 10:41:45.532651','2025-07-31 10:41:45.532665',NULL,1),(55,'IT Helpdesk Technician','Datalex','Dublin, County Dublin, Ireland','https://ie.linkedin.com/jobs/view/it-helpdesk-technician-at-datalex-4275354898','LINKEDIN','Remote','2025-07-31 10:41:45.781281','2025-07-31 10:41:45.781295',NULL,1),(56,'IT Helpdesk Support','Tactiq','Midlothian, VA','https://www.linkedin.com/jobs/view/it-helpdesk-support-at-tactiq-4275600923','LINKEDIN','Remote','2025-07-31 10:41:45.891647','2025-07-31 10:41:45.891661',NULL,1),(57,'IT Helpdesk Specialist Tier I','McKinney Specialty Labs','Richmond, VA','https://www.linkedin.com/jobs/view/it-helpdesk-specialist-tier-i-at-mckinney-specialty-labs-4273540186','LINKEDIN','Remote','2025-07-31 10:41:46.182426','2025-07-31 10:41:46.182440',NULL,1),(58,'IT Support Technician, Level 1','Bitfarms','Grove City, PA','https://www.linkedin.com/jobs/view/it-support-technician-level-1-at-bitfarms-4269697772','LINKEDIN','Remote','2025-07-31 10:41:46.586628','2025-07-31 10:41:46.586642',NULL,1),(59,'Tier I IT Help Desk','City of Windsor','Windsor, Ontario, Canada','https://ca.linkedin.com/jobs/view/tier-i-it-help-desk-at-city-of-windsor-4275850195','LINKEDIN','Remote','2025-07-31 10:41:46.991721','2025-07-31 10:41:46.991736',NULL,1),(60,'IT Support Technician','Cavista Technologies','Nigeria','https://ng.linkedin.com/jobs/view/it-support-technician-at-cavista-technologies-4273850150','LINKEDIN','Remote','2025-07-31 10:41:47.180993','2025-07-31 10:41:47.181007',NULL,1),(61,'IT Support Services II-Help Desk','Palmetto Technology Group (PTG)','Tucson, AZ','https://www.linkedin.com/jobs/view/it-support-services-ii-help-desk-at-palmetto-technology-group-ptg-4275408821','LINKEDIN','Remote','2025-07-31 10:41:47.341023','2025-07-31 10:41:47.341039',NULL,1),(62,'IT Workstation Technician Tier 1','Sante Health System, Inc','Fresno, CA','https://www.linkedin.com/jobs/view/it-workstation-technician-tier-1-at-sante-health-system-inc-4277466156','LINKEDIN','Remote','2025-07-31 10:41:47.648673','2025-07-31 10:41:47.648686',NULL,1),(63,'IT Desktop Support Technician - Tier I','Fuel Cycle','Los Angeles, CA','https://www.linkedin.com/jobs/view/it-desktop-support-technician-tier-i-at-fuel-cycle-4278393640','LINKEDIN','Remote','2025-07-31 10:41:47.815546','2025-07-31 10:41:47.815560',NULL,1),(64,'IT Support Technician','Lightmatter','Boston, MA','https://www.linkedin.com/jobs/view/it-support-technician-at-lightmatter-4274347930','LINKEDIN','Remote','2025-07-31 10:41:48.150365','2025-07-31 10:41:48.150380',NULL,1),(65,'Junior Support Engineer (L1 Support)','n8n','United Kingdom','https://uk.linkedin.com/jobs/view/junior-support-engineer-l1-support-at-n8n-4278391755','LINKEDIN','Remote','2025-07-31 10:41:47.959788','2025-07-31 10:41:47.959803',NULL,1),(66,'IT Helpdesk Technician','AutoPayPlus','Orlando, FL','https://www.linkedin.com/jobs/view/it-helpdesk-technician-at-autopayplus-4277872356','LINKEDIN','Remote','2025-07-31 10:41:48.406405','2025-07-31 10:41:48.406419',NULL,1),(67,'IT Support Engineer','LSH Auto UK Limited','Stockport, England, United Kingdom','https://uk.linkedin.com/jobs/view/it-support-engineer-at-lsh-auto-uk-limited-4275575717','LINKEDIN','Remote','2025-07-31 10:41:48.763172','2025-07-31 10:41:48.763186',NULL,1),(68,'IT Help Desk','Cutting Edge Network Technologies, An IT Solutions Company','Maitland, FL','https://www.linkedin.com/jobs/view/it-help-desk-at-cutting-edge-network-technologies-an-it-solutions-company-4272826403','LINKEDIN','Remote','2025-07-31 10:41:48.994885','2025-07-31 10:41:48.994899',NULL,1),(69,'IT Support Engineer','Sophos','Dallas, TX','https://www.linkedin.com/jobs/view/it-support-engineer-at-sophos-4277262757','LINKEDIN','Remote','2025-07-31 10:41:49.232324','2025-07-31 10:41:49.232338',NULL,1),(70,'Junior Support Engineer (L1 Support)','n8n','Portugal','https://pt.linkedin.com/jobs/view/junior-support-engineer-l1-support-at-n8n-4278390801','LINKEDIN','Remote','2025-07-31 10:41:49.500219','2025-07-31 10:41:49.500233',NULL,1),(71,'IT Support Technician','Maxime\'s','New York, NY','https://www.linkedin.com/jobs/view/it-support-technician-at-maxime-s-4272820096','LINKEDIN','Remote','2025-07-31 10:41:49.929324','2025-07-31 10:41:49.929339',NULL,1),(72,'Estágio em Documentação  (452452) - REMOTE','Touch Tecnologia','Brazil','https://br.linkedin.com/jobs/view/est%C3%A1gio-em-documenta%C3%A7%C3%A3o-452452-remote-at-touch-tecnologia-4278023576','LINKEDIN','Remote','2025-07-31 10:41:50.264258','2025-07-31 10:41:50.264273',NULL,1),(73,'Internship - IT Operations [RID-00553]','Setel','Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia','https://my.linkedin.com/jobs/view/internship-it-operations-rid-00553-at-setel-4264575366','LINKEDIN','Remote','2025-07-31 10:41:50.762003','2025-07-31 10:41:50.762018',NULL,1),(74,'IT Support Technician','Outerspace','Fairless Hills, PA','https://www.linkedin.com/jobs/view/it-support-technician-at-outerspace-4273502983','LINKEDIN','Remote','2025-07-31 10:41:51.139958','2025-07-31 10:41:51.139972',NULL,1),(75,'Junior Support Engineer (L1 Support)','n8n','Ireland','https://ie.linkedin.com/jobs/view/junior-support-engineer-l1-support-at-n8n-4278395364','LINKEDIN','Remote','2025-07-31 10:41:49.706853','2025-07-31 10:41:49.706868',NULL,1),(76,'IT Support Specialist','Umanova SA','Kemptthal, Zurich, Switzerland','https://ch.linkedin.com/jobs/view/it-support-specialist-at-umanova-sa-4275926113','LINKEDIN','Remote','2025-07-31 10:41:52.019748','2025-07-31 10:41:52.019763',NULL,1),(77,'IT Analyst Technician','NHS Scotland','Tan Office, England, United Kingdom','https://uk.linkedin.com/jobs/view/it-analyst-technician-at-nhs-scotland-4273769654','LINKEDIN','Remote','2025-07-31 10:41:52.195723','2025-07-31 10:41:52.195738',NULL,1),(78,'Senior IT Support Officer','Queensland Government','Brisbane, Queensland, Australia','https://au.linkedin.com/jobs/view/senior-it-support-officer-at-queensland-government-4277493550','LINKEDIN','Remote','2025-07-31 10:41:52.463126','2025-07-31 10:41:52.463141',NULL,1),(79,'IT Technician','Royal Electric Company','Sacramento, CA','https://www.linkedin.com/jobs/view/it-technician-at-royal-electric-company-4277830663','LINKEDIN','Remote','2025-07-31 10:41:52.729746','2025-07-31 10:41:52.729760',NULL,1),(80,'IT Support Specialist II','TechMD','Santa Ana, CA','https://www.linkedin.com/jobs/view/it-support-specialist-ii-at-techmd-4275479115','LINKEDIN','Remote','2025-07-31 10:41:52.956992','2025-07-31 10:41:52.957006',NULL,1),(81,'Support Engineer - IT Helpdesk','N3XT','United States','https://www.linkedin.com/jobs/view/support-engineer-it-helpdesk-at-n3xt-4273552363','LINKEDIN','Remote','2025-07-31 10:41:53.107736','2025-07-31 10:41:53.107751',NULL,1),(82,'IT Support Specialist II','TechMD','Auburn, MA','https://www.linkedin.com/jobs/view/it-support-specialist-ii-at-techmd-4277228216','LINKEDIN','Remote','2025-07-31 10:41:53.252775','2025-07-31 10:41:53.252789',NULL,1),(83,'IT Support Engineer','ProductLife Group','Metro Manila','https://ph.linkedin.com/jobs/view/it-support-engineer-at-productlife-group-4271274420','LINKEDIN','Remote','2025-07-31 10:41:53.553669','2025-07-31 10:41:53.553683',NULL,1),(84,'Remote Data Entry Associate','Lensa','United States','https://www.linkedin.com/jobs/view/remote-data-entry-associate-at-lensa-4273838011','LINKEDIN','Remote','2025-07-31 10:41:51.633777','2025-07-31 10:41:51.633792',NULL,1),(85,'IT Support Engineer','LSH AUTO','Stockport, England, United Kingdom','https://uk.linkedin.com/jobs/view/it-support-engineer-at-lsh-auto-4272084982','LINKEDIN','Remote','2025-07-31 10:41:53.764658','2025-07-31 10:41:53.764727',NULL,1),(86,'Junior Support Engineer (L1 Support)','n8n','Croatia','https://hr.linkedin.com/jobs/view/junior-support-engineer-l1-support-at-n8n-4278392705','LINKEDIN','Remote','2025-07-31 10:41:54.057593','2025-07-31 10:41:54.057607',NULL,1),(87,'IT Support Engineer','Sophos','Bucharest, Bucharest, Romania','https://ro.linkedin.com/jobs/view/it-support-engineer-at-sophos-4276960662','LINKEDIN','Remote','2025-07-31 10:41:54.689055','2025-07-31 10:41:54.689070',NULL,1),(88,'Junior Support Engineer (L1 Support)','n8n','Italy','https://it.linkedin.com/jobs/view/junior-support-engineer-l1-support-at-n8n-4278393627','LINKEDIN','Remote','2025-07-31 10:41:55.246361','2025-07-31 10:41:55.246376',NULL,1),(89,'IT - (Remote)','Lensa','United States','https://www.linkedin.com/jobs/view/it-remote-at-lensa-4273834317','LINKEDIN','Remote','2025-07-31 10:41:54.386060','2025-07-31 10:41:54.386075',NULL,1),(90,'IT Support Specialist','Neurensic','Chicago, IL','https://www.linkedin.com/jobs/view/it-support-specialist-at-neurensic-4277431679','LINKEDIN','Remote','2025-07-31 10:41:55.446298','2025-07-31 10:41:55.446313',NULL,1),(91,'Junior Support Engineer (L1 Support)','n8n','Poland','https://pl.linkedin.com/jobs/view/junior-support-engineer-l1-support-at-n8n-4278389833','LINKEDIN','Remote','2025-07-31 10:41:55.723054','2025-07-31 10:41:55.723069',NULL,1),(92,'IT Support Associate','Frontier Psychiatry','United States','https://www.linkedin.com/jobs/view/it-support-associate-at-frontier-psychiatry-4277691637','LINKEDIN','Remote','2025-07-31 10:41:56.022825','2025-07-31 10:41:56.022839',NULL,1),(93,'IT Support Specialist','UnCruise Adventures Small Ship Cruising','Seattle, WA','https://www.linkedin.com/jobs/view/it-support-specialist-at-uncruise-adventures-small-ship-cruising-4273537484','LINKEDIN','Remote','2025-07-31 10:41:56.393140','2025-07-31 10:41:56.393154',NULL,1),(94,'IT Support Engineer','Summit Business Technologies','Millersville, MD','https://www.linkedin.com/jobs/view/it-support-engineer-at-summit-business-technologies-4270837290','LINKEDIN','Remote','2025-07-31 10:41:56.689991','2025-07-31 10:41:56.690006',NULL,1),(95,'Onsite IT Support Engineer','Storagepipe, a THRIVE Company','Singapore','https://sg.linkedin.com/jobs/view/onsite-it-support-engineer-at-storagepipe-a-thrive-company-4271770565','LINKEDIN','Remote','2025-07-31 10:41:56.902782','2025-07-31 10:41:56.902797',NULL,1),(96,'Junior Support Engineer (L1 Support)','n8n','Spain','https://es.linkedin.com/jobs/view/junior-support-engineer-l1-support-at-n8n-4278392697','LINKEDIN','Remote','2025-07-31 10:41:57.123460','2025-07-31 10:41:57.123475',NULL,1),(97,'IT Service Desk Analyst II','Olmsted Medical Center','Rochester, MN','https://www.linkedin.com/jobs/view/it-service-desk-analyst-ii-at-olmsted-medical-center-4270885399','LINKEDIN','Remote','2025-07-31 10:41:57.324637','2025-07-31 10:41:57.324651',NULL,1),(98,'IT Technician','Northwood Ravin','Charlotte, NC','https://www.linkedin.com/jobs/view/it-technician-at-northwood-ravin-4272473897','LINKEDIN','Remote','2025-07-31 10:41:57.602366','2025-07-31 10:41:57.602380',NULL,1),(99,'Desktop support technician','nLeague','Warrenton, VA','https://www.linkedin.com/jobs/view/desktop-support-technician-at-nleague-4275710563','LINKEDIN','Remote','2025-07-31 10:41:57.902595','2025-07-31 10:41:57.902609',NULL,1),(100,'Jr. Systems Administrator','Frontier IT','Colorado Springs, CO','https://www.linkedin.com/jobs/view/jr-systems-administrator-at-frontier-it-4271768659','LINKEDIN','Remote','2025-07-31 10:41:58.035707','2025-07-31 10:41:58.035721',NULL,1),(101,'IT & Security Administrator','Bitwarden','Santa Barbara, CA','https://www.linkedin.com/jobs/view/it-security-administrator-at-bitwarden-4278522305','LINKEDIN','Remote','2025-07-31 10:22:44.606320','2025-07-31 10:22:44.606335',NULL,1),(102,'IT Operations Technician','Sophos','Bucharest, Bucharest, Romania','https://ro.linkedin.com/jobs/view/it-operations-technician-at-sophos-4276963138','LINKEDIN','Remote','2025-07-31 10:41:58.549663','2025-07-31 10:41:58.549677',NULL,1),(103,'IT Support Engineer','Sécheron Hasler Group','Satigny, Geneva, Switzerland','https://ch.linkedin.com/jobs/view/it-support-engineer-at-s%C3%A9cheron-hasler-group-4273223748','LINKEDIN','Remote','2025-07-31 10:41:58.885311','2025-07-31 10:41:58.885326',NULL,1),(104,'IT Service Desk Analyst','Simplify','St Ives, England, United Kingdom','https://uk.linkedin.com/jobs/view/it-service-desk-analyst-at-simplify-4270311677','LINKEDIN','Remote','2025-07-31 10:41:59.059177','2025-07-31 10:41:59.059192',NULL,1),(105,'IT Support Specialist- Full Time','Achievement Centers for Children','Westlake, OH','https://www.linkedin.com/jobs/view/it-support-specialist-full-time-at-achievement-centers-for-children-4275757307','LINKEDIN','Remote','2025-07-31 10:41:58.269603','2025-07-31 10:41:58.269618',NULL,1),(106,'IT Helpdesk Engineer','Tradeling','Dubai, Dubai, United Arab Emirates','https://ae.linkedin.com/jobs/view/it-helpdesk-engineer-at-tradeling-4272109125','LINKEDIN','Remote','2025-07-31 10:22:47.328071','2025-07-31 10:22:47.328086',NULL,1),(107,'Software Engineer, Backend','Tinder','Palo Alto, CA','https://www.linkedin.com/jobs/view/software-engineer-backend-at-tinder-4259594855','LINKEDIN','Remote','2025-07-31 10:42:32.498232','2025-07-31 10:42:32.498247',NULL,1),(108,'Software Engineer, Backend','Tinder','San Francisco, CA','https://www.linkedin.com/jobs/view/software-engineer-backend-at-tinder-4259593912','LINKEDIN','Remote','2025-07-31 10:42:32.853287','2025-07-31 10:42:32.853301',NULL,1),(109,'Software Engineer, Frontend','DoorDash','Pune, Maharashtra, India','https://in.linkedin.com/jobs/view/software-engineer-frontend-at-doordash-4248552076','LINKEDIN','Remote','2025-07-31 10:42:33.222079','2025-07-31 10:42:33.222094',NULL,1),(110,'Frontend Engineer (React)','CRED','United States','https://www.linkedin.com/jobs/view/frontend-engineer-react-at-cred-4278391780','LINKEDIN','Remote','2025-07-31 10:42:08.096765','2025-07-31 10:42:08.096780',NULL,1),(111,'Software Engineer','Beautiful.ai','San Francisco, CA','https://www.linkedin.com/jobs/view/software-engineer-at-beautiful-ai-4277898262','LINKEDIN','Remote','2025-07-31 10:42:34.876372','2025-07-31 10:42:34.876387',NULL,1),(112,'Software Engineer','DoorDash','London, England, United Kingdom','https://uk.linkedin.com/jobs/view/software-engineer-at-doordash-4275039261','LINKEDIN','Remote','2025-07-31 10:42:33.974163','2025-07-31 10:42:33.974177',NULL,1),(113,'Software Engineer, Frontend - Canada','DoorDash','Toronto, Ontario, Canada','https://ca.linkedin.com/jobs/view/software-engineer-frontend-canada-at-doordash-4229281507','LINKEDIN','Remote','2025-07-31 10:42:41.656203','2025-07-31 10:42:41.656218',NULL,1),(114,'Back End Engineer I','Pearpop','United States','https://www.linkedin.com/jobs/view/back-end-engineer-i-at-pearpop-4278394985','LINKEDIN','Remote','2025-07-31 10:42:36.821451','2025-07-31 10:42:36.821465',NULL,1),(115,'Frontend Engineer (React)','CRED','United Kingdom','https://uk.linkedin.com/jobs/view/frontend-engineer-react-at-cred-4278392745','LINKEDIN','Remote','2025-07-31 10:42:09.497666','2025-07-31 10:42:09.497680',NULL,1),(116,'Software Developer Junior based in U.S.A','Advancio','United States','https://www.linkedin.com/jobs/view/software-developer-junior-based-in-u-s-a-at-advancio-4273754798','LINKEDIN','Remote','2025-07-31 10:42:34.999376','2025-07-31 10:42:34.999391',NULL,1),(117,'Software Engineer (Frontend)','Twilio','United Kingdom','https://uk.linkedin.com/jobs/view/software-engineer-frontend-at-twilio-4251421293','LINKEDIN','Remote','2025-07-31 10:42:10.344117','2025-07-31 10:42:10.344132',NULL,1),(118,'Software Engineer – Entry Level (Remote)','Jobright.ai','San Francisco Bay Area','https://www.linkedin.com/jobs/view/software-engineer-%E2%80%93-entry-level-remote-at-jobright-ai-4273208440','LINKEDIN','Remote','2025-07-31 10:42:10.887372','2025-07-31 10:42:10.887387',NULL,1),(119,'Software Engineer','ServiceNow','Santa Clara, CA','https://www.linkedin.com/jobs/view/software-engineer-at-servicenow-4277434364','LINKEDIN','Remote','2025-07-31 10:42:11.430359','2025-07-31 10:42:11.430373',NULL,1),(120,'Software Engineer','NowSecure','United States','https://www.linkedin.com/jobs/view/software-engineer-at-nowsecure-4275057536','LINKEDIN','Remote','2025-07-31 10:42:36.014313','2025-07-31 10:42:36.014327',NULL,1),(121,'Software Engineer','Nourish','New York, NY','https://www.linkedin.com/jobs/view/software-engineer-at-nourish-4246782478','LINKEDIN','Remote','2025-07-31 10:42:12.029809','2025-07-31 10:42:12.029824',NULL,1),(122,'Software Engineering Intern','Verse','San Francisco, CA','https://www.linkedin.com/jobs/view/software-engineering-intern-at-verse-4275559057','LINKEDIN','Remote','2025-07-31 10:42:12.432842','2025-07-31 10:42:12.432858',NULL,1),(123,'Software Engineer Fullstack (entry level)','Twilio','Estonia','https://ee.linkedin.com/jobs/view/software-engineer-fullstack-entry-level-at-twilio-4261002767','LINKEDIN','Remote','2025-07-31 10:42:37.386071','2025-07-31 10:42:37.386085',NULL,1),(124,'Software Engineer - Frontend','Experian','Hyderabad, Telangana, India','https://in.linkedin.com/jobs/view/software-engineer-frontend-at-experian-4264793115','LINKEDIN','Remote','2025-07-31 10:42:33.794173','2025-07-31 10:42:33.794187',NULL,1),(125,'Junior Developer','Summit Sky Consulting','Minneapolis, MN','https://www.linkedin.com/jobs/view/junior-developer-at-summit-sky-consulting-4272085792','LINKEDIN','Remote','2025-07-31 10:42:36.179766','2025-07-31 10:42:36.179780',NULL,1),(126,'Software Engineer','Docusign','Seattle, WA','https://www.linkedin.com/jobs/view/software-engineer-at-docusign-4246735598','LINKEDIN','Remote','2025-07-31 10:42:13.574443','2025-07-31 10:42:13.574459',NULL,1),(127,'[Full Remote] Junior Developer Front-End (Desenvolvedor Front-End Júnior)','Joinrs','Brazil','https://br.linkedin.com/jobs/view/full-remote-junior-developer-front-end-desenvolvedor-front-end-j%C3%BAnior-at-joinrs-4276610483','LINKEDIN','Remote','2025-07-31 10:42:34.181009','2025-07-31 10:42:34.181025',NULL,1),(128,'Javascript Developer - Remote Work','BairesDev','Bangalore Urban, Karnataka, India','https://in.linkedin.com/jobs/view/javascript-developer-remote-work-at-bairesdev-4271830871','LINKEDIN','Remote','2025-07-31 10:42:46.725827','2025-07-31 10:42:46.725841',NULL,1),(129,'Frontend Engineer (React)','CRED','Brazil','https://br.linkedin.com/jobs/view/frontend-engineer-react-at-cred-4278392746','LINKEDIN','Remote','2025-07-31 10:42:14.393401','2025-07-31 10:42:14.393416',NULL,1),(130,'Junior Developer','Summit Sky Consulting','Allentown, PA','https://www.linkedin.com/jobs/view/junior-developer-at-summit-sky-consulting-4272091547','LINKEDIN','Remote','2025-07-31 10:42:37.153106','2025-07-31 10:42:37.153121',NULL,1),(131,'Software Engineer I - Remote','Duck Creek Technologies','India','https://in.linkedin.com/jobs/view/software-engineer-i-remote-at-duck-creek-technologies-4232503400','LINKEDIN','Remote','2025-07-31 10:42:47.955744','2025-07-31 10:42:47.955758',NULL,1),(132,'Junior Full Stack Developer','24x7 Direct','Metro Manila','https://ph.linkedin.com/jobs/view/junior-full-stack-developer-at-24x7-direct-4278079292','LINKEDIN','Remote','2025-07-31 10:42:35.506001','2025-07-31 10:42:35.506189',NULL,1),(133,'Software Engineer I','Tripadvisor','Waterloo, Ontario, Canada','https://ca.linkedin.com/jobs/view/software-engineer-i-at-tripadvisor-4273280928','LINKEDIN','Remote','2025-07-31 10:42:15.822596','2025-07-31 10:42:15.822610',NULL,1),(134,'Javascript Developer - Remote Work','BairesDev','Bengaluru, Karnataka, India','https://in.linkedin.com/jobs/view/javascript-developer-remote-work-at-bairesdev-4271831748','LINKEDIN','Remote','2025-07-31 10:42:49.497015','2025-07-31 10:42:49.497029',NULL,1),(135,'Software Engineer 0','Onyx Point, LLC.','Hanover, MD','https://www.linkedin.com/jobs/view/software-engineer-0-at-onyx-point-llc-4275421313','LINKEDIN','Remote','2025-07-31 10:42:16.289730','2025-07-31 10:42:16.289746',NULL,1),(136,'Full Stack Developer','Veracity Software Inc','New Jersey, United States','https://www.linkedin.com/jobs/view/full-stack-developer-at-veracity-software-inc-4272186371','LINKEDIN','Remote','2025-07-31 10:42:36.579985','2025-07-31 10:42:36.580000',NULL,1),(137,'Software Engineer','Leidos','United States','https://www.linkedin.com/jobs/view/software-engineer-at-leidos-4272779148','LINKEDIN','Remote','2025-07-31 10:42:16.681384','2025-07-31 10:42:16.681398',NULL,1),(138,'Software Engineer','Two Barrels LLC','Spokane Valley, WA','https://www.linkedin.com/jobs/view/software-engineer-at-two-barrels-llc-4273286517','LINKEDIN','Remote','2025-07-31 10:42:16.967761','2025-07-31 10:42:16.967776',NULL,1),(139,'Web Developer, Entry Level, (Remote)','Jobright.ai','United States','https://www.linkedin.com/jobs/view/web-developer-entry-level-remote-at-jobright-ai-4273067619','LINKEDIN','Remote','2025-07-31 10:42:17.189927','2025-07-31 10:42:17.189942',NULL,1),(140,'Software Engineer II, Backend','DoorDash','Toronto, Ontario, Canada','https://ca.linkedin.com/jobs/view/software-engineer-ii-backend-at-doordash-3980018979','LINKEDIN','Remote','2025-07-31 10:42:43.358554','2025-07-31 10:42:43.358568',NULL,1),(141,'Software Engineer (UK)','The Hustle','London, England, United Kingdom','https://uk.linkedin.com/jobs/view/software-engineer-uk-at-the-hustle-4276990523','LINKEDIN','Remote','2025-07-31 10:42:46.260996','2025-07-31 10:42:46.261024',NULL,1),(142,'Full Stack Engineer','Remarcable','United States','https://www.linkedin.com/jobs/view/full-stack-engineer-at-remarcable-4272830723','LINKEDIN','Remote','2025-07-31 10:42:17.758785','2025-07-31 10:42:17.758799',NULL,1),(143,'Software Engineer','SHI International Corp.','Austin, TX','https://www.linkedin.com/jobs/view/software-engineer-at-shi-international-corp-4270132452','LINKEDIN','Remote','2025-07-31 10:42:18.113561','2025-07-31 10:42:18.113576',NULL,1),(144,'Software Engineer','Experian','Hyderabad, Telangana, India','https://in.linkedin.com/jobs/view/software-engineer-at-experian-4264716029','LINKEDIN','Remote','2025-07-31 10:42:33.605799','2025-07-31 10:42:33.605813',NULL,1),(145,'Software Engineer, Frontend (Entry Level) (Remote)','Jobright.ai','United States','https://www.linkedin.com/jobs/view/software-engineer-frontend-entry-level-remote-at-jobright-ai-4273072373','LINKEDIN','Remote','2025-07-31 10:42:18.794217','2025-07-31 10:42:18.794232',NULL,1),(146,'Software Engineer','Docusign','Seattle, WA','https://www.linkedin.com/jobs/view/software-engineer-at-docusign-4217793985','LINKEDIN','Remote','2025-07-31 10:42:19.223977','2025-07-31 10:42:19.223993',NULL,1),(147,'Javascript Developer - Remote Work','BairesDev','Delhi, India','https://in.linkedin.com/jobs/view/javascript-developer-remote-work-at-bairesdev-4271832706','LINKEDIN','Remote','2025-07-31 10:42:19.459731','2025-07-31 10:42:19.459745',NULL,1),(148,'Software Engineer (UK)','HubSpot Ventures','London, England, United Kingdom','https://uk.linkedin.com/jobs/view/software-engineer-uk-at-hubspot-ventures-4273237633','LINKEDIN','Remote','2025-07-31 10:42:19.738722','2025-07-31 10:42:19.738738',NULL,1),(149,'Software Development Engineer, Adobe FireFly','Adobe','San Jose, CA','https://www.linkedin.com/jobs/view/software-development-engineer-adobe-firefly-at-adobe-4272841947','LINKEDIN','Remote','2025-07-31 10:42:20.250438','2025-07-31 10:42:20.250453',NULL,1),(150,'Frontend Web Developer, Entry Level, (Remote)','Jobright.ai','United States','https://www.linkedin.com/jobs/view/frontend-web-developer-entry-level-remote-at-jobright-ai-4273061125','LINKEDIN','Remote','2025-07-31 10:42:20.461757','2025-07-31 10:42:20.461772',NULL,1),(151,'Entegral Software Engineer - Remote','Entegral','United States','https://www.linkedin.com/jobs/view/entegral-software-engineer-remote-at-entegral-4275055738','LINKEDIN','Remote','2025-07-31 10:42:43.879189','2025-07-31 10:42:43.879203',NULL,1),(152,'Frontend Software Engineer, Growth Engineering','Postman','San Francisco, CA','https://www.linkedin.com/jobs/view/frontend-software-engineer-growth-engineering-at-postman-4208725848','LINKEDIN','Remote','2025-07-31 10:42:38.483952','2025-07-31 10:42:38.483967',NULL,1),(153,'Frontend Engineer','MoonPay','London, England, United Kingdom','https://uk.linkedin.com/jobs/view/frontend-engineer-at-moonpay-4275580784','LINKEDIN','Remote','2025-07-31 10:42:20.990489','2025-07-31 10:42:20.990504',NULL,1),(154,'Software Engineer (Entry Level) (Remote)','Jobright.ai','United States','https://www.linkedin.com/jobs/view/software-engineer-entry-level-remote-at-jobright-ai-4273052889','LINKEDIN','Remote','2025-07-31 10:42:21.693389','2025-07-31 10:42:21.693404',NULL,1),(155,'Software Engineer 0 w/ Java','Onyx Point, LLC.','Hanover, MD','https://www.linkedin.com/jobs/view/software-engineer-0-w-java-at-onyx-point-llc-4275419624','LINKEDIN','Remote','2025-07-31 10:42:22.018681','2025-07-31 10:42:22.018696',NULL,1),(156,'Software Engineer, Backend','Cresta','Toronto, Ontario, Canada','https://ca.linkedin.com/jobs/view/software-engineer-backend-at-cresta-4218881194','LINKEDIN','Remote','2025-07-31 10:42:45.872075','2025-07-31 10:42:45.872089',NULL,1),(157,'Javascript Developer - Remote Work','BairesDev','Hyderabad, Telangana, India','https://in.linkedin.com/jobs/view/javascript-developer-remote-work-at-bairesdev-4271832852','LINKEDIN','Remote','2025-07-31 10:42:22.607423','2025-07-31 10:42:22.607439',NULL,1),(158,'[Full Remote] Junior Web Developer','Joinrs','United States','https://www.linkedin.com/jobs/view/full-remote-junior-web-developer-at-joinrs-4276616493','LINKEDIN','Remote','2025-07-31 10:42:38.302767','2025-07-31 10:42:38.302782',NULL,1),(159,'Frontend Software Engineer - TikTok Live - 2025 Start','TikTok','Singapore, Singapore','https://sg.linkedin.com/jobs/view/frontend-software-engineer-tiktok-live-2025-start-at-tiktok-4076512111','LINKEDIN','Remote','2025-07-31 10:42:23.277417','2025-07-31 10:42:23.277450',NULL,1),(160,'Full Stack Software Engineer','Ford Motor Company','United States','https://www.linkedin.com/jobs/view/full-stack-software-engineer-at-ford-motor-company-4278388569','LINKEDIN','Remote','2025-07-31 10:42:24.196083','2025-07-31 10:42:24.196098',NULL,1),(161,'Frontend Developer','Zen','India','https://in.linkedin.com/jobs/view/frontend-developer-at-zen-4273020010','LINKEDIN','Remote','2025-07-31 10:42:39.940830','2025-07-31 10:42:39.940844',NULL,1),(162,'Software Engineer - Full Stack','Orbis Group','New York, NY','https://www.linkedin.com/jobs/view/software-engineer-full-stack-at-orbis-group-4271479967','LINKEDIN','Remote','2025-07-31 10:42:24.494081','2025-07-31 10:42:24.494096',NULL,1),(163,'Software Engineer, Google Cloud Web3','Google','Sunnyvale, CA','https://www.linkedin.com/jobs/view/software-engineer-google-cloud-web3-at-google-4260156901','LINKEDIN','Remote','2025-07-31 10:42:24.683039','2025-07-31 10:42:24.683055',NULL,1),(164,'Software Engineer – Entry Level (Remote)','Jobright.ai','Seattle, WA','https://www.linkedin.com/jobs/view/software-engineer-%E2%80%93-entry-level-remote-at-jobright-ai-4273206566','LINKEDIN','Remote','2025-07-31 10:42:25.173109','2025-07-31 10:42:25.173125',NULL,1),(165,'Junior Full-Stack Software Engineer (Remote)','Jobright.ai','United States','https://www.linkedin.com/jobs/view/junior-full-stack-software-engineer-remote-at-jobright-ai-4275058827','LINKEDIN','Remote','2025-07-31 10:42:23.879440','2025-07-31 10:42:23.879455',NULL,1),(166,'Backend Software Engineer, Observability','Wing','Palo Alto, CA','https://www.linkedin.com/jobs/view/backend-software-engineer-observability-at-wing-4236127969','LINKEDIN','Remote','2025-07-31 10:42:25.418532','2025-07-31 10:42:25.418547',NULL,1),(167,'React Developer','Infosys','Chennai, Tamil Nadu, India','https://in.linkedin.com/jobs/view/react-developer-at-infosys-4273507456','LINKEDIN','Remote','2025-07-31 10:42:34.423935','2025-07-31 10:42:34.423949',NULL,1),(168,'Web UI Engineer (L5) - Netflix Game Controller - Games Player Experiences','Netflix','United States','https://www.linkedin.com/jobs/view/web-ui-engineer-l5-netflix-game-controller-games-player-experiences-at-netflix-4187551494','LINKEDIN','Remote','2025-07-31 10:42:34.677156','2025-07-31 10:42:34.677170',NULL,1),(169,'Backend Developer, Pakistan','VinAudit.com Inc.','Islamabad, Islāmābād, Pakistan','https://pk.linkedin.com/jobs/view/backend-developer-pakistan-at-vinaudit-com-inc-4272851155','LINKEDIN','Remote','2025-07-31 10:42:35.187152','2025-07-31 10:42:35.187167',NULL,1),(170,'Frontend Developer','SourcingScreen','India','https://in.linkedin.com/jobs/view/frontend-developer-at-sourcingscreen-4273070953','LINKEDIN','Remote','2025-07-31 10:42:35.770891','2025-07-31 10:42:35.770904',NULL,1),(171,'JavaScript','TestUnity','India','https://in.linkedin.com/jobs/view/javascript-at-testunity-4273063583','LINKEDIN','Remote','2025-07-31 10:42:36.986083','2025-07-31 10:42:36.986098',NULL,1),(172,'Frontend Developer (React)','Alex Staff','Türkiye','https://tr.linkedin.com/jobs/view/frontend-developer-react-at-alex-staff-4277617514','LINKEDIN','Remote','2025-07-31 10:42:37.718866','2025-07-31 10:42:37.718880',NULL,1),(173,'Javascript Frontend Developer','SourcingScreen','United Arab Emirates','https://ae.linkedin.com/jobs/view/javascript-frontend-developer-at-sourcingscreen-4274040652','LINKEDIN','Remote','2025-07-31 10:42:37.907139','2025-07-31 10:42:37.907154',NULL,1),(174,'Software Engineer','Concentrix Catalyst','Bengaluru, Karnataka, India','https://in.linkedin.com/jobs/view/software-engineer-at-concentrix-catalyst-4275634343','LINKEDIN','Remote','2025-07-31 10:42:38.116008','2025-07-31 10:42:38.116104',NULL,1),(175,'JavaScript Developer (Pixi.js)','GoReel','Bratislava, Bratislava, Slovakia','https://sk.linkedin.com/jobs/view/javascript-developer-pixi-js-at-goreel-4277631047','LINKEDIN','Remote','2025-07-31 10:42:38.790624','2025-07-31 10:42:38.790638',NULL,1),(176,'Frontend Developer (React)','Alex Staff','Kazakhstan','https://kz.linkedin.com/jobs/view/frontend-developer-react-at-alex-staff-4277617515','LINKEDIN','Remote','2025-07-31 10:42:39.164786','2025-07-31 10:42:39.164800',NULL,1),(177,'Junior Software Engineer/Developer','Spalding, a Saalex company','Lexington Park, MD','https://www.linkedin.com/jobs/view/junior-software-engineer-developer-at-spalding-a-saalex-company-4275629331','LINKEDIN','Remote','2025-07-31 10:42:39.607074','2025-07-31 10:42:39.607088',NULL,1),(178,'Software Engineer I [T500-19390]','Best Buy™ India','Bengaluru, Karnataka, India','https://in.linkedin.com/jobs/view/software-engineer-i-t500-19390-at-best-buy%E2%84%A2-india-4275630567','LINKEDIN','Remote','2025-07-31 10:42:40.352298','2025-07-31 10:42:40.352313',NULL,1),(179,'Full Stack Engineer','Capgemini Engineering','Bengaluru, Karnataka, India','https://in.linkedin.com/jobs/view/full-stack-engineer-at-capgemini-engineering-4275085543','LINKEDIN','Remote','2025-07-31 10:42:40.813137','2025-07-31 10:42:40.813153',NULL,1),(180,'Software Developer','Colegio Suizo de México','Blackburn, England, United Kingdom','https://uk.linkedin.com/jobs/view/software-developer-at-colegio-suizo-de-m%C3%A9xico-4273374491','LINKEDIN','Remote','2025-07-31 10:42:41.312504','2025-07-31 10:42:41.312519',NULL,1),(181,'Software Engineer I','Cummins India','Pune, Maharashtra, India','https://in.linkedin.com/jobs/view/software-engineer-i-at-cummins-india-4273722129','LINKEDIN','Remote','2025-07-31 10:42:42.429664','2025-07-31 10:42:42.429678',NULL,1),(182,'JavaScript Developer (Pixi.js)','GoReel','Warsaw, Mazowieckie, Poland','https://pl.linkedin.com/jobs/view/javascript-developer-pixi-js-at-goreel-4277629327','LINKEDIN','Remote','2025-07-31 10:42:43.080897','2025-07-31 10:42:43.080911',NULL,1),(183,'Junior Full Stack Developer','Harmonia Holdings Group, LLC','McLean, VA','https://www.linkedin.com/jobs/view/junior-full-stack-developer-at-harmonia-holdings-group-llc-4278519658','LINKEDIN','Remote','2025-07-31 10:42:44.254480','2025-07-31 10:42:44.254494',NULL,1),(184,'AI First Developer','Smartcat','Lisboa, Lisbon, Portugal','https://pt.linkedin.com/jobs/view/ai-first-developer-at-smartcat-4277441646','LINKEDIN','Remote','2025-07-31 10:42:44.481068','2025-07-31 10:42:44.481082',NULL,1),(185,'Backend Engineer, Core Technology','Stripe','San Francisco, CA','https://www.linkedin.com/jobs/view/backend-engineer-core-technology-at-stripe-4190706249','LINKEDIN','Remote','2025-07-31 10:42:44.973927','2025-07-31 10:42:44.973941',NULL,1),(186,'Java  Developer','Abmiro','Pune, Maharashtra, India','https://in.linkedin.com/jobs/view/java-developer-at-abmiro-4272053858','LINKEDIN','Remote','2025-07-31 10:42:45.406332','2025-07-31 10:42:45.406347',NULL,1),(187,'Distributed Systems Engineer (L4) - Data Platform','Netflix','United States','https://www.linkedin.com/jobs/view/distributed-systems-engineer-l4-data-platform-at-netflix-3993679179','LINKEDIN','Remote','2025-07-31 10:42:46.029945','2025-07-31 10:42:46.029987',NULL,1),(188,'Software Developer-Backend','Emerson','Noida, Uttar Pradesh, India','https://in.linkedin.com/jobs/view/software-developer-backend-at-emerson-4250602171','LINKEDIN','Remote','2025-07-31 10:42:46.449661','2025-07-31 10:42:46.449676',NULL,1),(189,'Full Stack Web Developer','OMO Digital','Pune, Maharashtra, India','https://in.linkedin.com/jobs/view/full-stack-web-developer-at-omo-digital-4273559920','LINKEDIN','Remote','2025-07-31 10:42:46.890596','2025-07-31 10:42:46.890610',NULL,1),(190,'JavaScript Developer (Pixi.js)','GoReel','Romania','https://ro.linkedin.com/jobs/view/javascript-developer-pixi-js-at-goreel-4277630098','LINKEDIN','Remote','2025-07-31 10:42:47.065585','2025-07-31 10:42:47.065599',NULL,1),(191,'Software Engineer, UI (C#)','Oak Engage','Newcastle Upon Tyne, England, United Kingdom','https://uk.linkedin.com/jobs/view/software-engineer-ui-c%23-at-oak-engage-4277807919','LINKEDIN','Remote','2025-07-31 10:42:47.247116','2025-07-31 10:42:47.247130',NULL,1),(192,'JavaScript Developer (Pixi.js)','GoReel','Ukraine','https://ua.linkedin.com/jobs/view/javascript-developer-pixi-js-at-goreel-4277624918','LINKEDIN','Remote','2025-07-31 10:42:47.507932','2025-07-31 10:42:47.507947',NULL,1),(193,'Front-end Engineer','Vectara','Pakistan','https://pk.linkedin.com/jobs/view/front-end-engineer-at-vectara-4278096477','LINKEDIN','Remote','2025-07-31 10:42:47.701126','2025-07-31 10:42:47.701140',NULL,1),(194,'Backend Developer (Java & Python)','Weekday AI (YC W21)','Bengaluru, Karnataka, India','https://in.linkedin.com/jobs/view/backend-developer-java-python-at-weekday-ai-yc-w21-4276678579','LINKEDIN','Remote','2025-07-31 10:42:48.159062','2025-07-31 10:42:48.159076',NULL,1),(195,'Frontend Developer (React)','Alex Staff','Georgia','https://ge.linkedin.com/jobs/view/frontend-developer-react-at-alex-staff-4277613831','LINKEDIN','Remote','2025-07-31 10:42:48.422321','2025-07-31 10:42:48.422335',NULL,1),(196,'Full Stack Software Engineer (TypeScript/React)','OneImaging','Canada','https://ca.linkedin.com/jobs/view/full-stack-software-engineer-typescript-react-at-oneimaging-4278339936','LINKEDIN','Remote','2025-07-31 10:42:48.754148','2025-07-31 10:42:48.754162',NULL,1),(197,'Backend Developer (NestJs)','UltaHost','Bangladesh','https://bd.linkedin.com/jobs/view/backend-developer-nestjs-at-ultahost-4273512543','LINKEDIN','Remote','2025-07-31 10:42:48.998001','2025-07-31 10:42:48.998016',NULL,1),(198,'Full Stack JavaScript Developer I AI Start Up','TheDriveGroup','New South Wales, Australia','https://au.linkedin.com/jobs/view/full-stack-javascript-developer-i-ai-start-up-at-thedrivegroup-4272006414','LINKEDIN','Remote','2025-07-31 10:42:49.219426','2025-07-31 10:42:49.219441',NULL,1),(199,'Software Engineer, Platform (C#)','Oak Engage','Newcastle Upon Tyne, England, United Kingdom','https://uk.linkedin.com/jobs/view/software-engineer-platform-c%23-at-oak-engage-4277808912','LINKEDIN','Remote','2025-07-31 10:42:49.730989','2025-07-31 10:42:49.731669',NULL,1),(200,'Data Analyst, Product','Chime','San Francisco, CA','https://www.linkedin.com/jobs/view/data-analyst-product-at-chime-4249701623','LINKEDIN','Remote','2025-07-31 10:42:56.656634','2025-07-31 10:42:56.656649',NULL,1),(201,'Data Analyst','KOHO','Canada','https://ca.linkedin.com/jobs/view/data-analyst-at-koho-4261768641','LINKEDIN','Remote','2025-07-31 10:42:56.974371','2025-07-31 10:42:56.974386',NULL,1),(202,'Data Analyst, Reporting & Operations','Publicis Groupe UK','London, England, United Kingdom','https://uk.linkedin.com/jobs/view/data-analyst-reporting-operations-at-publicis-groupe-uk-4221294140','LINKEDIN','Remote','2025-07-31 10:42:57.800494','2025-07-31 10:42:57.800509',NULL,1),(203,'Data Analyst','Marwood Group','New York, United States','https://www.linkedin.com/jobs/view/data-analyst-at-marwood-group-4275459660','LINKEDIN','Remote','2025-07-31 10:42:58.222047','2025-07-31 10:42:58.222062',NULL,1),(204,'Data Analyst','Zipliens','Charlotte, NC','https://www.linkedin.com/jobs/view/data-analyst-at-zipliens-4270102203','LINKEDIN','Remote','2025-07-31 10:42:58.920551','2025-07-31 10:42:58.920567',NULL,1),(205,'Business Intelligence Data Analyst','Zeal Group','London, England, United Kingdom','https://uk.linkedin.com/jobs/view/business-intelligence-data-analyst-at-zeal-group-4152713556','LINKEDIN','Remote','2025-07-31 10:42:59.210347','2025-07-31 10:42:59.210361',NULL,1),(206,'Data Analyst','Smile Train','New York City Metropolitan Area','https://www.linkedin.com/jobs/view/data-analyst-at-smile-train-4260189706','LINKEDIN','Remote','2025-07-31 10:42:59.853414','2025-07-31 10:42:59.853429',NULL,1),(207,'Data Analyst','Fynora Ai','New York City Metropolitan Area','https://www.linkedin.com/jobs/view/data-analyst-at-fynora-ai-4278342269','LINKEDIN','Remote','2025-07-31 10:43:00.010229','2025-07-31 10:43:00.010244',NULL,1),(208,'Data Analyst','Anthos|Home','New York, NY','https://www.linkedin.com/jobs/view/data-analyst-at-anthos-home-4275851090','LINKEDIN','Remote','2025-07-31 10:43:00.520030','2025-07-31 10:43:00.520044',NULL,1),(209,'Product Data Analyst','NinjaTrader','United States','https://www.linkedin.com/jobs/view/product-data-analyst-at-ninjatrader-4278381144','LINKEDIN','Remote','2025-07-31 10:43:00.996814','2025-07-31 10:43:00.996829',NULL,1),(210,'Senior Data Analyst','Coalition, Inc.','Canada','https://ca.linkedin.com/jobs/view/senior-data-analyst-at-coalition-inc-4250433819','LINKEDIN','Remote','2025-07-31 10:43:01.264654','2025-07-31 10:43:01.264669',NULL,1),(211,'Senior Data Analyst','Coalition, Inc.','United States','https://www.linkedin.com/jobs/view/senior-data-analyst-at-coalition-inc-4250433818','LINKEDIN','Remote','2025-07-31 10:43:01.729239','2025-07-31 10:43:01.729253',NULL,1),(212,'Associate Data Analyst','Experian','Sofia, Sofia City, Bulgaria','https://bg.linkedin.com/jobs/view/associate-data-analyst-at-experian-4261485149','LINKEDIN','Remote','2025-07-31 10:43:01.940536','2025-07-31 10:43:01.940551',NULL,1),(213,'Sr. Data Analyst','SmartLight Analytics','Plano, TX','https://www.linkedin.com/jobs/view/sr-data-analyst-at-smartlight-analytics-4278386966','LINKEDIN','Remote','2025-07-31 10:43:02.305979','2025-07-31 10:43:02.305994',NULL,1),(214,'Junior Data Analyst','e-Careers','Solihull, England, United Kingdom','https://uk.linkedin.com/jobs/view/junior-data-analyst-at-e-careers-4272089615','LINKEDIN','Remote','2025-07-31 10:43:02.702322','2025-07-31 10:43:02.702336',NULL,1),(215,'Junior Data Analyst (Identity and Fraud)','Experian','Sofia, Sofia City, Bulgaria','https://bg.linkedin.com/jobs/view/junior-data-analyst-identity-and-fraud-at-experian-4261485165','LINKEDIN','Remote','2025-07-31 10:43:03.422377','2025-07-31 10:43:03.422392',NULL,1),(216,'Data Analyst (PBM)','Liviniti','United States','https://www.linkedin.com/jobs/view/data-analyst-pbm-at-liviniti-4278076458','LINKEDIN','Remote','2025-07-31 10:43:04.125991','2025-07-31 10:43:04.126006',NULL,1),(217,'Data Analyst, Marketing Analytics','Rover.com','Barcelona, Catalonia, Spain','https://es.linkedin.com/jobs/view/data-analyst-marketing-analytics-at-rover-com-4237669405','LINKEDIN','Remote','2025-07-31 10:43:04.636204','2025-07-31 10:43:04.636219',NULL,1),(218,'Data Analyst','DarkStar Intelligence','Arlington, VA','https://www.linkedin.com/jobs/view/data-analyst-at-darkstar-intelligence-4278389291','LINKEDIN','Remote','2025-07-31 10:43:05.835108','2025-07-31 10:43:05.835123',NULL,1),(219,'Data Analyst','Capgemini','Melbourne, Victoria, Australia','https://au.linkedin.com/jobs/view/data-analyst-at-capgemini-4264576985','LINKEDIN','Remote','2025-07-31 10:43:04.804421','2025-07-31 10:43:04.804436',NULL,1),(220,'Data Analyst','HelloFresh','Toronto, Ontario, Canada','https://ca.linkedin.com/jobs/view/data-analyst-at-hellofresh-4275087567','LINKEDIN','Remote','2025-07-31 10:43:07.068884','2025-07-31 10:43:07.068899',NULL,1),(221,'Data Analyst','173tech','London Area, United Kingdom','https://uk.linkedin.com/jobs/view/data-analyst-at-173tech-4278064804','LINKEDIN','Remote','2025-07-31 10:43:05.196732','2025-07-31 10:43:05.196748',NULL,1),(222,'Sr Insights & Analytics Analyst','Nintendo','Redmond, WA','https://www.linkedin.com/jobs/view/sr-insights-analytics-analyst-at-nintendo-4264266093','LINKEDIN','Remote','2025-07-31 10:43:05.513531','2025-07-31 10:43:05.513545',NULL,1),(223,'Remote: Data Visualization Specialist','IntePros','United States','https://www.linkedin.com/jobs/view/remote-data-visualization-specialist-at-intepros-4271741416','LINKEDIN','Remote','2025-07-31 10:43:06.023925','2025-07-31 10:43:06.023939',NULL,1),(224,'Data Analyst','Excel™','United States','https://www.linkedin.com/jobs/view/data-analyst-at-excel%E2%84%A2-4277822237','LINKEDIN','Remote','2025-07-31 10:43:06.316825','2025-07-31 10:43:06.316840',NULL,1),(225,'Data Analyst','Tag','India','https://in.linkedin.com/jobs/view/data-analyst-at-tag-4273399920','LINKEDIN','Remote','2025-07-31 10:43:06.867508','2025-07-31 10:43:06.867523',NULL,1),(226,'Data Analyst (Remote)','BTI Executive Search','WP. Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia','https://my.linkedin.com/jobs/view/data-analyst-remote-at-bti-executive-search-4273528926','LINKEDIN','Remote','2025-07-31 10:43:07.577967','2025-07-31 10:43:07.577981',NULL,1),(227,'Data Analyst II - (Remote - US)','Mediavine','Atlanta, GA','https://www.linkedin.com/jobs/view/data-analyst-ii-remote-us-at-mediavine-4250030229','LINKEDIN','Remote','2025-07-31 10:43:08.066697','2025-07-31 10:43:08.066712',NULL,1),(228,'Junior Data Analyst','SteerBridge','Washington, DC','https://www.linkedin.com/jobs/view/junior-data-analyst-at-steerbridge-4277859872','LINKEDIN','Remote','2025-07-31 10:43:08.324623','2025-07-31 10:43:08.324637',NULL,1),(229,'Data Analyst','Fortress Information Security','Greater Orlando','https://www.linkedin.com/jobs/view/data-analyst-at-fortress-information-security-4271861640','LINKEDIN','Remote','2025-07-31 10:43:08.825626','2025-07-31 10:43:08.825641',NULL,1),(230,'Data Analyst','IntelliPro','Sunnyvale, CA','https://www.linkedin.com/jobs/view/data-analyst-at-intellipro-4273862102','LINKEDIN','Remote','2025-07-31 10:43:08.588769','2025-07-31 10:43:08.588783',NULL,1),(231,'Data Analyst – Junior (Remote)','Jobright.ai','Glencoe, IL','https://www.linkedin.com/jobs/view/data-analyst-%E2%80%93-junior-remote-at-jobright-ai-4273209412','LINKEDIN','Remote','2025-07-31 10:43:09.265845','2025-07-31 10:43:09.265860',NULL,1),(232,'Data Analyst','DMI','Ohio, United States','https://www.linkedin.com/jobs/view/data-analyst-at-dmi-4261024309','LINKEDIN','Remote','2025-07-31 10:43:09.524099','2025-07-31 10:43:09.524113',NULL,1),(233,'Business Intelligence Data Analyst','Zeal Group','Sofia, Sofia City, Bulgaria','https://bg.linkedin.com/jobs/view/business-intelligence-data-analyst-at-zeal-group-4152712720','LINKEDIN','Remote','2025-07-31 10:43:09.722054','2025-07-31 10:43:09.722128',NULL,1),(234,'Data Entry Analyst','Granicus India','Bengaluru, Karnataka, India','https://in.linkedin.com/jobs/view/data-entry-analyst-at-granicus-india-4273854295','LINKEDIN','Remote','2025-07-31 10:43:09.943296','2025-07-31 10:43:09.943311',NULL,1),(235,'Business Intelligence Data Analyst','Zeal Group','Belgrade, Serbia','https://rs.linkedin.com/jobs/view/business-intelligence-data-analyst-at-zeal-group-4152712731','LINKEDIN','Remote','2025-07-31 10:43:10.954188','2025-07-31 10:43:10.954204',NULL,1),(236,'Data Analyst','KCS iT','Lisbon, Portugal','https://pt.linkedin.com/jobs/view/data-analyst-at-kcs-it-4273702796','LINKEDIN','Remote','2025-07-31 10:43:11.246085','2025-07-31 10:43:11.246099',NULL,1),(237,'Data Analyst (Healthcare)','Vaco by Highspring','Tampa, FL','https://www.linkedin.com/jobs/view/data-analyst-healthcare-at-vaco-by-highspring-4278086276','LINKEDIN','Remote','2025-07-31 10:43:11.642668','2025-07-31 10:43:11.642683',NULL,1),(238,'Data Analyst','PANGEATWO','Birmingham, AL','https://www.linkedin.com/jobs/view/data-analyst-at-pangeatwo-4275460864','LINKEDIN','Remote','2025-07-31 10:43:11.877319','2025-07-31 10:43:11.877339',NULL,1),(239,'Business Intelligence Analyst','Boulay','Eden Prairie, MN','https://www.linkedin.com/jobs/view/business-intelligence-analyst-at-boulay-4275414235','LINKEDIN','Remote','2025-07-31 10:43:12.145890','2025-07-31 10:43:12.145905',NULL,1),(240,'Graduate Data Analyst','Bending Spoons','London, England, United Kingdom','https://uk.linkedin.com/jobs/view/graduate-data-analyst-at-bending-spoons-4274301969','LINKEDIN','Remote','2025-07-31 10:43:12.708667','2025-07-31 10:43:12.708681',NULL,1),(241,'Data Analyst','Bending Spoons','London, England, United Kingdom','https://uk.linkedin.com/jobs/view/data-analyst-at-bending-spoons-4273548832','LINKEDIN','Remote','2025-07-31 10:43:13.174140','2025-07-31 10:43:13.174154',NULL,1),(242,'Data Analyst','IXIS','United States','https://www.linkedin.com/jobs/view/data-analyst-at-ixis-4274303511','LINKEDIN','Remote','2025-07-31 10:43:14.040059','2025-07-31 10:43:14.040073',NULL,1),(243,'Data Analyst, Entry Level, (Remote)','TapTalent.ai','Richmond, VA','https://www.linkedin.com/jobs/view/data-analyst-entry-level-remote-at-taptalent-ai-4277671952','LINKEDIN','Remote','2025-07-31 10:43:14.331190','2025-07-31 10:43:14.331205',NULL,1),(244,'Senior Product Data Analyst','ZOE','United Kingdom','https://uk.linkedin.com/jobs/view/senior-product-data-analyst-at-zoe-4262434417','LINKEDIN','Remote','2025-07-31 10:43:14.718897','2025-07-31 10:43:14.718911',NULL,1),(245,'Data Analyst','Bitso','Latin America','https://www.linkedin.com/jobs/view/data-analyst-at-bitso-4264500736','LINKEDIN','Remote','2025-07-31 10:43:15.088674','2025-07-31 10:43:15.088689',NULL,1),(246,'Data Analyst Lead','Leavitt Industrial Group','Coquitlam, British Columbia, Canada','https://ca.linkedin.com/jobs/view/data-analyst-lead-at-leavitt-industrial-group-4273781742','LINKEDIN','Remote','2025-07-31 10:24:09.210189','2025-07-31 10:24:09.210205',NULL,1),(247,'Telecom Data Analyst','Pearce Services','United States','https://www.linkedin.com/jobs/view/telecom-data-analyst-at-pearce-services-4278372864','LINKEDIN','Remote','2025-07-31 10:43:15.410413','2025-07-31 10:43:15.410427',NULL,1),(248,'Intelligence Analyst','Everbridge','Hungary','https://hu.linkedin.com/jobs/view/intelligence-analyst-at-everbridge-4273591986','LINKEDIN','Remote','2025-07-31 10:43:15.611191','2025-07-31 10:43:15.611206',NULL,1),(249,'Data Engineer','City of Oxnard','Oxnard, CA','https://www.linkedin.com/jobs/view/data-engineer-at-city-of-oxnard-4275732722','LINKEDIN','Remote','2025-07-31 10:24:10.603150','2025-07-31 10:24:10.603164',NULL,1),(250,'Data Analyst','Matritel','Hungary','https://hu.linkedin.com/jobs/view/data-analyst-at-matritel-4277663276','LINKEDIN','Remote','2025-07-31 10:43:15.907673','2025-07-31 10:43:15.907688',NULL,1),(251,'Jr. Data Analyst','Beacon Hill','Dallas, TX','https://www.linkedin.com/jobs/view/jr-data-analyst-at-beacon-hill-4272810782','LINKEDIN','Remote','2025-07-31 10:43:16.110899','2025-07-31 10:43:16.110914',NULL,1),(252,'Business Intelligence Analyst','Engine','United States','https://www.linkedin.com/jobs/view/business-intelligence-analyst-at-engine-4264267112','LINKEDIN','Remote','2025-07-31 10:43:16.412559','2025-07-31 10:43:16.412573',NULL,1),(253,'Data Analyst, Entry Level, (Remote)','Jobright.ai','United States','https://www.linkedin.com/jobs/view/data-analyst-entry-level-remote-at-jobright-ai-4273291876','LINKEDIN','Remote','2025-07-31 10:43:16.684206','2025-07-31 10:43:16.684221',NULL,1),(254,'Data Analyst','TapTalent.ai','Chicago, IL','https://www.linkedin.com/jobs/view/data-analyst-at-taptalent-ai-4277671932','LINKEDIN','Remote','2025-07-31 10:43:16.884861','2025-07-31 10:43:16.884875',NULL,1),(255,'Data Analyst, Entry Level, (Remote)','Jobright.ai','United States','https://www.linkedin.com/jobs/view/data-analyst-entry-level-remote-at-jobright-ai-4273533255','LINKEDIN','Remote','2025-07-31 10:43:17.073373','2025-07-31 10:43:17.073387',NULL,1),(256,'Salesforce Business & Data Analyst','Sandisk','Irvine, CA','https://www.linkedin.com/jobs/view/salesforce-business-data-analyst-at-sandisk-4275783913','LINKEDIN','Remote','2025-07-31 10:43:17.428570','2025-07-31 10:43:17.428585',NULL,1),(257,'Data Analyst','Wiraa','United States','https://www.linkedin.com/jobs/view/data-analyst-at-wiraa-4278398900','LINKEDIN','Remote','2025-07-31 10:24:12.626513','2025-07-31 10:24:12.626527',NULL,1),(258,'Data Analyst, New Grad (Remote)','Jobright.ai','United States','https://www.linkedin.com/jobs/view/data-analyst-new-grad-remote-at-jobright-ai-4274349641','LINKEDIN','Remote','2025-07-31 10:43:17.894483','2025-07-31 10:43:17.894498',NULL,1),(259,'Senior GenAI Specialist','Wise and Agile Solutions Limited','Nairobi, Nairobi County, Kenya','https://ke.linkedin.com/jobs/view/senior-genai-specialist-at-wise-and-agile-solutions-limited-4273889562','LINKEDIN','Kenya','2025-07-31 10:41:29.268039','2025-07-31 10:41:29.268055',NULL,1),(260,'Junior Support Engineer (L1 Support)','n8n','Bulgaria','https://bg.linkedin.com/jobs/view/junior-support-engineer-l1-support-at-n8n-4278394339','LINKEDIN','Remote','2025-07-31 10:41:54.933302','2025-07-31 10:41:54.933316',NULL,1),(261,'Data Engineering Analyst, Remote','Experian','California, United States','https://www.linkedin.com/jobs/view/data-engineering-analyst-remote-at-experian-4269682761','LINKEDIN','Remote','2025-07-31 10:43:10.332539','2025-07-31 10:43:10.332553',NULL,1),(262,'Data Insights Analyst - Healthcare ( remote ) ( remote )','Lensa','Orlando, FL','https://www.linkedin.com/jobs/view/data-insights-analyst-healthcare-remote-remote-at-lensa-4273831110','LINKEDIN','Remote','2025-07-31 10:43:18.294710','2025-07-31 10:43:18.294723',NULL,1),(263,'Lead Data Analyst','James Search Group','United States','https://www.linkedin.com/jobs/view/lead-data-analyst-at-james-search-group-4275888965','LINKEDIN','Remote','2025-07-31 10:43:18.816717','2025-07-31 10:43:18.816733',NULL,1),(264,'Senior Data Analyst','KOHO','Canada','https://ca.linkedin.com/jobs/view/senior-data-analyst-at-koho-4261768639','LINKEDIN','Remote','2025-07-31 10:43:19.182641','2025-07-31 10:43:19.182655',NULL,1);
/*!40000 ALTER TABLE `job_scraper_joblisting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_seeker`
--

DROP TABLE IF EXISTS `job_seeker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_seeker` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `github_url` varchar(255) DEFAULT NULL,
  `linkedin_url` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `bioData` longtext,
  `about` longtext,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `users_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_id` (`users_id`),
  CONSTRAINT `job_seeker_users_id_63a8b78c_fk_users_id` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_seeker`
--

LOCK TABLES `job_seeker` WRITE;
/*!40000 ALTER TABLE `job_seeker` DISABLE KEYS */;
INSERT INTO `job_seeker` VALUES (1,'https://github.com','httt://linkedn.com','Nairobi,Kenya','backend developer with 3+ years of experience in Node.js, MongoDB, and REST APIs. | I am a backend developer passionate about building scalable and reliable systems. I enjoy working with startups and small businesses to create meaningful software solutions','','2025-07-29 13:15:56.557322','2025-07-29 13:26:59.290175',2),(2,'http://www.github.com','','Nairobi,Kenya',NULL,'','2025-07-30 14:48:39.944349','2025-07-30 14:48:39.944424',3);
/*!40000 ALTER TABLE `job_seeker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobseeker_certification`
--

DROP TABLE IF EXISTS `jobseeker_certification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobseeker_certification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `issuer` varchar(45) DEFAULT NULL,
  `uploadPath` varchar(500) DEFAULT NULL,
  `awardedDate` date DEFAULT NULL,
  `description` longtext,
  `userId` bigint DEFAULT NULL,
  `createdAt` datetime(6) DEFAULT NULL,
  `updatedAt` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `jobseeker_certification_userId_75e40c46_fk_users_id` (`userId`),
  CONSTRAINT `jobseeker_certification_userId_75e40c46_fk_users_id` FOREIGN KEY (`userId`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobseeker_certification`
--

LOCK TABLES `jobseeker_certification` WRITE;
/*!40000 ALTER TABLE `jobseeker_certification` DISABLE KEYS */;
INSERT INTO `jobseeker_certification` VALUES (1,'Amazon Web Services (AWS)','https://www.instagram.com','2025-07-01','Validates expertise in designing distributed systems on AWS, covering cloud architecture best practices, security, scalability, and cost optimization.',2,NULL,NULL),(2,'Google (via Coursera)','https://www.instagram.com','2025-06-09','A beginner-friendly certification teaching data cleaning, analysis, visualization (using tools like SQL, Tableau, and R), and data-driven decision-making',2,NULL,NULL);
/*!40000 ALTER TABLE `jobseeker_certification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruiter`
--

DROP TABLE IF EXISTS `recruiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recruiter` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `companyName` varchar(45) NOT NULL,
  `companyLogo` varchar(500) DEFAULT NULL,
  `industry` varchar(250) DEFAULT NULL,
  `contactInfo` varchar(250) DEFAULT NULL,
  `companyEmail` varchar(254) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `isVerified` tinyint(1) DEFAULT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `users_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyEmail` (`companyEmail`),
  KEY `recruiter_users_id_d9d3bf72_fk_users_id` (`users_id`),
  CONSTRAINT `recruiter_users_id_d9d3bf72_fk_users_id` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter`
--

LOCK TABLES `recruiter` WRITE;
/*!40000 ALTER TABLE `recruiter` DISABLE KEYS */;
INSERT INTO `recruiter` VALUES (1,'Eujim Solution',NULL,'Tech','eujim@gmail.com','eujim@hr.com','Looking for talented developers',NULL,'2025-07-29 16:57:55.195934','2025-07-29 16:59:05.689298',4);
/*!40000 ALTER TABLE `recruiter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruiter_doc`
--

DROP TABLE IF EXISTS `recruiter_doc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recruiter_doc` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `verifiedAt` datetime(6) DEFAULT NULL,
  `doc_type` varchar(45) DEFAULT NULL,
  `upload_path` varchar(100) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `recruiter_id` bigint DEFAULT NULL,
  `verifiedBy_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `recruiter_doc_verifiedBy_id_8f87e472_fk_users_id` (`verifiedBy_id`),
  CONSTRAINT `recruiter_doc_verifiedBy_id_8f87e472_fk_users_id` FOREIGN KEY (`verifiedBy_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter_doc`
--

LOCK TABLES `recruiter_doc` WRITE;
/*!40000 ALTER TABLE `recruiter_doc` DISABLE KEYS */;
INSERT INTO `recruiter_doc` VALUES (1,'2025-07-29 17:03:49.012076','registration certificate','recruiter_docs/2025/07/29/07conductingmarketresearch.pdf','approved','2025-07-29 17:02:55.043573','2025-07-29 17:03:49.029360',1,1);
/*!40000 ALTER TABLE `recruiter_doc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruiter_tracking`
--

DROP TABLE IF EXISTS `recruiter_tracking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recruiter_tracking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_type` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `notes` longtext,
  `interviewDate` datetime(6) DEFAULT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `job_posting_id` bigint DEFAULT NULL,
  `job_seeker_id` bigint DEFAULT NULL,
  `recruiter_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `recruiter_tracking_job_posting_id_86a9b208_fk_job_postings_id` (`job_posting_id`),
  CONSTRAINT `recruiter_tracking_job_posting_id_86a9b208_fk_job_postings_id` FOREIGN KEY (`job_posting_id`) REFERENCES `job_postings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter_tracking`
--

LOCK TABLES `recruiter_tracking` WRITE;
/*!40000 ALTER TABLE `recruiter_tracking` DISABLE KEYS */;
INSERT INTO `recruiter_tracking` VALUES (1,'recruiter','hired','Interested in JavaScript, Node.js skills','2025-01-08 00:00:00.000000','2025-07-29 17:01:32.788209','2025-07-30 14:18:34.333784',NULL,1,1),(2,'recruiter','applied','Applied via Easy Apply on Job Feeds','2025-01-01 00:00:00.000000','2025-07-30 14:30:06.700814','2025-07-30 14:30:06.700868',1,1,1),(3,'recruiter','applied','Applied via Easy Apply on Job Feeds','2025-01-01 00:00:00.000000','2025-07-30 14:49:31.545679','2025-07-30 14:49:31.545725',1,2,1);
/*!40000 ALTER TABLE `recruiter_tracking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skillSet`
--

DROP TABLE IF EXISTS `skillSet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skillSet` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `proffeciency_level` varchar(20) DEFAULT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `skill_id` bigint DEFAULT NULL,
  `userId` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `skillSet_skill_id_31be97b4_fk_skills_id` (`skill_id`),
  KEY `skillSet_userId_edfe9896_fk_users_id` (`userId`),
  CONSTRAINT `skillSet_skill_id_31be97b4_fk_skills_id` FOREIGN KEY (`skill_id`) REFERENCES `skills` (`id`),
  CONSTRAINT `skillSet_userId_edfe9896_fk_users_id` FOREIGN KEY (`userId`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skillSet`
--

LOCK TABLES `skillSet` WRITE;
/*!40000 ALTER TABLE `skillSet` DISABLE KEYS */;
INSERT INTO `skillSet` VALUES (1,'intermediate','2025-07-29 13:27:23.284129','2025-07-29 13:27:23.284202',1,2),(2,'begginner','2025-07-30 14:46:47.747785','2025-07-30 14:46:47.747859',3,2),(3,'proffessional','2025-07-30 14:48:58.076591','2025-07-30 14:48:58.076666',4,3);
/*!40000 ALTER TABLE `skillSet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills`
--

DROP TABLE IF EXISTS `skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skills` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `skillName` varchar(45) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
INSERT INTO `skills` VALUES (1,'React',''),(2,'python',''),(3,'MySql',''),(4,'Java','');
/*!40000 ALTER TABLE `skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `lastName` varchar(150) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `isStaff` tinyint(1) NOT NULL,
  `isSuperuser` tinyint(1) NOT NULL,
  `lastLogin` datetime(6) DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `is_suspended` tinyint(1) NOT NULL,
  `is_pending` tinyint(1) NOT NULL,
  `isVerified` tinyint(1) NOT NULL,
  `verificationCode` char(32) DEFAULT NULL,
  `role` varchar(20) DEFAULT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `dateJoined` datetime(6) NOT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `deletion_reason` longtext,
  `deleted_by_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `users_deleted_by_id_d342c553_fk_users_id` (`deleted_by_id`),
  CONSTRAINT `users_deleted_by_id_d342c553_fk_users_id` FOREIGN KEY (`deleted_by_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Martin','Kinoti','martin@gmail.com','pbkdf2_sha256$600000$Z5GVlIIcdtg37wET25XOvX$RXLwUKy7CkDxj/Xtnn5VoEh1zbpZfN4541g3uHioaNI=',1,0,0,NULL,0,0,1,1,'e2f708a86b6c4a8dae7c00c952e5e8e9','superAdmin','2025-07-28 12:22:45.922417','2025-07-28 14:37:57.939113','2025-07-28 12:22:45.922544',NULL,NULL,NULL),(2,'Bien','ManSoul','mansoul@gmail.com','pbkdf2_sha256$600000$hQizuISGXtDL9UoL7Z0gWz$nKGWB4G+FmWUuU/Sp37uKAh2YJV9lMsxZsJL1P/5KSA=',1,0,0,NULL,0,0,1,1,'793532dd5f5540fd973d695ad5322674','jobseeker','2025-07-28 14:40:41.859071','2025-07-28 14:45:48.916426','2025-07-28 14:40:41.948602',NULL,NULL,NULL),(3,'Samson','Kiplong','kiplong@gmail.com','pbkdf2_sha256$600000$nIuKPuoq0EBeMsEiXQPZnG$xP19XSX5p3fXkGxDm3VizAZbfYeGnvIZKUioGhGWk6s=',1,0,0,NULL,0,0,1,1,'0b03b033767a4fba913ca94c8b5caea3','jobseeker','2025-07-28 14:43:19.118141','2025-07-28 14:45:36.681662','2025-07-28 14:43:19.118253',NULL,NULL,NULL),(4,'Antony','Kimei','kimei@gmail.com','pbkdf2_sha256$600000$nQQGrPz3GZ2FPxg5IMNGNn$Lwgr6AhtInDMmTo983u+OBpl3T0Hxa5zuFwlx5JYC7s=',1,0,0,NULL,0,0,1,1,'f30567b9a8a946ba8d2705054260ca63','employer','2025-07-28 14:48:06.300493','2025-07-29 15:44:47.861191','2025-07-28 14:48:06.300601',NULL,NULL,NULL),(5,'Peter','Thiel','peter@gmail.com','pbkdf2_sha256$600000$fvkLVFnh8MidrwnZ7oD2Z8$OwhoXn92rFxcvp9psp+udHDKC4gck2TBBblQ15u2u6A=',1,0,0,NULL,0,0,1,1,'dba88396cba6489ca4deb530421d8881','admin','2025-07-29 11:19:59.962804','2025-07-29 11:20:40.209547','2025-07-29 11:19:59.962924',NULL,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_groups`
--

DROP TABLE IF EXISTS `users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_groups_user_id_group_id_fc7788e8_uniq` (`user_id`,`group_id`),
  KEY `users_groups_group_id_2f3517aa_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_groups_group_id_2f3517aa_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_groups_user_id_f500bee5_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_groups`
--

LOCK TABLES `users_groups` WRITE;
/*!40000 ALTER TABLE `users_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_permissions`
--

DROP TABLE IF EXISTS `users_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_permissions_user_id_permission_id_3b86cbdf_uniq` (`user_id`,`permission_id`),
  KEY `users_user_permissio_permission_id_6d08dcd2_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_permissio_permission_id_6d08dcd2_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_permissions_user_id_92473840_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_permissions`
--

LOCK TABLES `users_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-31 15:32:22
