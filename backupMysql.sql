-- MySQL dump 10.13  Distrib 8.0.42, for Linux (x86_64)
--
-- Host: localhost    Database: eujimSolution
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
) ENGINE=InnoDB DEFAULT CHARSET=big5;
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
) ENGINE=InnoDB DEFAULT CHARSET=big5;
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
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add job seeker',8,'add_jobseeker'),(30,'Can change job seeker',8,'change_jobseeker'),(31,'Can delete job seeker',8,'delete_jobseeker'),(32,'Can view job seeker',8,'view_jobseeker'),(33,'Can add job seeker certification',9,'add_jobseekercertification'),(34,'Can change job seeker certification',9,'change_jobseekercertification'),(35,'Can delete job seeker certification',9,'delete_jobseekercertification'),(36,'Can view job seeker certification',9,'view_jobseekercertification'),(37,'Can add skill',10,'add_skill'),(38,'Can change skill',10,'change_skill'),(39,'Can delete skill',10,'delete_skill'),(40,'Can view skill',10,'view_skill'),(41,'Can add skill set',11,'add_skillset'),(42,'Can change skill set',11,'change_skillset'),(43,'Can delete skill set',11,'delete_skillset'),(44,'Can view skill set',11,'view_skillset'),(45,'Can add recruiter',12,'add_recruiter'),(46,'Can change recruiter',12,'change_recruiter'),(47,'Can delete recruiter',12,'delete_recruiter'),(48,'Can view recruiter',12,'view_recruiter'),(49,'Can add recruiter doc',13,'add_recruiterdoc'),(50,'Can change recruiter doc',13,'change_recruiterdoc'),(51,'Can delete recruiter doc',13,'delete_recruiterdoc'),(52,'Can view recruiter doc',13,'view_recruiterdoc'),(53,'Can add recruiter tracking',14,'add_recruitertracking'),(54,'Can change recruiter tracking',14,'change_recruitertracking'),(55,'Can delete recruiter tracking',14,'delete_recruitertracking'),(56,'Can view recruiter tracking',14,'view_recruitertracking'),(57,'Can add education',15,'add_education'),(58,'Can change education',15,'change_education'),(59,'Can delete education',15,'delete_education'),(60,'Can view education',15,'view_education'),(61,'Can add job posting',16,'add_jobposting'),(62,'Can change job posting',16,'change_jobposting'),(63,'Can delete job posting',16,'delete_jobposting'),(64,'Can view job posting',16,'view_jobposting'),(65,'Can add job posting skill',17,'add_jobpostingskill'),(66,'Can change job posting skill',17,'change_jobpostingskill'),(67,'Can delete job posting skill',17,'delete_jobpostingskill'),(68,'Can view job posting skill',17,'view_jobpostingskill');
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
) ENGINE=InnoDB DEFAULT CHARSET=big5;
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
) ENGINE=InnoDB DEFAULT CHARSET=big5;
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
) ENGINE=InnoDB DEFAULT CHARSET=big5;
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
) ENGINE=InnoDB DEFAULT CHARSET=big5;
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(15,'jobseeker','education'),(8,'jobseeker','jobseeker'),(9,'jobseeker','jobseekercertification'),(16,'job_posting','jobposting'),(17,'job_posting','jobpostingskill'),(12,'recruiter','recruiter'),(13,'recruiter','recruiterdoc'),(14,'recruiter','recruitertracking'),(6,'sessions','session'),(10,'skills','skill'),(11,'skills','skillset'),(7,'users','user');
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
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-05-15 09:22:11.878299'),(2,'auth','0001_initial','2025-05-15 09:23:53.948290'),(3,'admin','0001_initial','2025-05-15 09:24:07.564897'),(4,'admin','0002_logentry_remove_auto_add','2025-05-15 09:24:07.796385'),(5,'admin','0003_logentry_add_action_flag_choices','2025-05-15 09:24:08.205006'),(6,'contenttypes','0002_remove_content_type_name','2025-05-15 09:24:17.924144'),(7,'auth','0002_alter_permission_name_max_length','2025-05-15 09:24:22.971538'),(8,'auth','0003_alter_user_email_max_length','2025-05-15 09:24:28.175217'),(9,'auth','0004_alter_user_username_opts','2025-05-15 09:24:28.635598'),(10,'auth','0005_alter_user_last_login_null','2025-05-15 09:24:32.806316'),(11,'auth','0006_require_contenttypes_0002','2025-05-15 09:24:32.962118'),(12,'auth','0007_alter_validators_add_error_messages','2025-05-15 09:24:33.352931'),(13,'auth','0008_alter_user_username_max_length','2025-05-15 09:24:39.889459'),(14,'auth','0009_alter_user_last_name_max_length','2025-05-15 09:24:45.499261'),(15,'auth','0010_alter_group_name_max_length','2025-05-15 09:24:55.213161'),(16,'auth','0011_update_proxy_permissions','2025-05-15 09:24:55.840145'),(17,'auth','0012_alter_user_first_name_max_length','2025-05-15 09:25:06.836508'),(18,'sessions','0001_initial','2025-05-15 09:25:14.080691'),(19,'jobseeker','0001_initial','2025-05-19 11:29:34.446181'),(20,'recruiter','0001_initial','2025-05-19 11:29:36.284047'),(21,'skills','0001_initial','2025-05-19 11:29:36.578781'),(22,'users','0001_initial','2025-05-19 11:29:36.954171'),(23,'users','0002_alter_user_options','2025-05-19 11:32:36.716450'),(24,'users','0003_alter_user_options','2025-05-19 11:47:01.362144'),(25,'users','0004_alter_user_options','2025-05-21 07:18:13.111064'),(26,'users','0005_user_deleted_at_user_deleted_by_user_deletion_reason_and_more','2025-05-21 10:42:26.331982'),(27,'jobseeker','0002_alter_jobseekercertification_options_education','2025-06-09 07:55:53.215738'),(28,'jobseeker','0003_jobseekercertification_user_and_more','2025-06-09 07:55:53.250935'),(29,'recruiter','0002_alter_recruiter_options_alter_recruiterdoc_options_and_more','2025-06-09 07:55:53.262379'),(30,'recruiter','0003_alter_recruiter_options_and_more','2025-06-09 07:55:53.272106'),(31,'recruiter','0004_alter_recruiter_options','2025-06-09 07:55:53.304518'),(32,'recruiter','0005_rename_company_email_recruiter_companyemail_and_more','2025-06-09 07:55:53.316482'),(33,'skills','0002_alter_skill_options_alter_skillset_options','2025-06-09 07:55:53.337876'),(34,'skills','0003_rename_skill_name_skill_skillname_and_more','2025-06-09 07:55:53.349723'),(35,'users','0002_alter_user_is_superuser_alter_user_last_login','2025-06-09 07:55:53.361219'),(36,'users','0006_merge_20250609_0657','2025-06-09 07:55:53.371258'),(37,'users','0007_alter_user_managers_remove_user_deleted_at_and_more','2025-06-09 07:55:53.384841'),(38,'users','0008_add_missing_fields','2025-06-09 07:55:53.393330'),(39,'users','0009_alter_user_is_superuser_alter_user_last_login','2025-06-09 07:55:53.404811'),(40,'users','0010_add_missing_fields','2025-06-09 07:55:53.437855'),(41,'users','0011_alter_user_last_login','2025-06-09 08:07:28.794636'),(42,'users','0012_alter_user_options_remove_user_secondname_and_more','2025-06-09 08:13:48.742975'),(43,'users','0013_remove_user_date_joined_remove_user_is_active_and_more','2025-06-09 08:22:54.373801'),(44,'users','0014_remove_user_first_name_remove_user_last_name','2025-06-09 08:25:32.926240'),(45,'users','0015_rename_secondname_user_lastname','2025-06-09 08:32:53.927698'),(46,'recruiter','0006_alter_recruiter_user_alter_recruiterdoc_verifiedby_and_more','2025-06-09 08:45:16.379930'),(47,'skills','0004_alter_skillset_user','2025-06-09 08:45:16.397415'),(48,'users','0002_user_is_active_alter_user_verificationcode','2025-06-11 07:32:08.468322'),(49,'recruiter','0007_fix_verifiedBy_column','2025-06-11 08:03:29.913256'),(50,'jobseeker','0004_rename_created_at_jobseekercertification_createdat_and_more','2025-06-16 13:04:00.945815'),(51,'recruiter','0008_alter_recruiterdoc_verifiedby_and_more','2025-06-16 13:04:01.327231'),(52,'job_posting','0001_initial','2025-07-02 09:01:19.782758'),(53,'recruiter','0009_recruitertracking_job_posting','2025-07-02 09:01:25.577969'),(54,'recruiter','0010_rename_job_posting_recruitertracking_job_posting_id_and_more','2025-07-02 09:01:26.164412'),(55,'users','0003_alter_user_options_user_datejoined_user_isstaff_and_more','2025-07-02 09:02:53.988443'),(56,'recruiter','0011_alter_recruitertracking_job_posting_id','2025-07-02 09:04:27.753657'),(57,'recruiter','0012_alter_recruitertracking_job_posting_id','2025-07-02 09:17:02.456902'),(58,'recruiter','0013_rename_job_posting_id_recruitertracking_job_posting','2025-07-02 09:17:56.418158'),(59,'recruiter','0014_recruitertracking_user_type','2025-07-07 07:47:02.402876'),(60,'recruiter','0015_recruitertracking_unique_job_application','2025-07-08 08:52:15.277562'),(61,'recruiter','0016_remove_recruitertracking_unique_job_application','2025-07-08 09:09:37.127140');
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
) ENGINE=InnoDB DEFAULT CHARSET=big5;
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
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `institution_name` varchar(100) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `degree` varchar(20) NOT NULL,
  `field_of_study` varchar(100) NOT NULL,
  `start_year` int unsigned NOT NULL,
  `end_year` int unsigned DEFAULT NULL,
  `is_current` tinyint(1) NOT NULL DEFAULT '0',
  `description` longtext,
  `school_logo` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `education_qualifications_user_id` (`user_id`),
  CONSTRAINT `education_qualifications_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `education_qualifications`
--

LOCK TABLES `education_qualifications` WRITE;
/*!40000 ALTER TABLE `education_qualifications` DISABLE KEYS */;
INSERT INTO `education_qualifications` VALUES (5,13,'University of Nairobi','Bachelor of Science','bachelor','Artificial Intelligence',2022,2026,0,'Specialized in Artificial Intelligence and Machine Learning','https://example.com/logos/university-tech.png','2025-06-09 09:01:49','2025-06-09 09:01:49'),(6,13,'Unversity of Nairobi','Bachelor of Science in Artificial Intelligence','bachelor','Software Engineering',2022,2024,0,'LEARNT ABOUT THE FUNDAMENTAL OF SOFTWARE ENGINEERINH','','2025-06-18 08:56:00','2025-06-18 08:56:00');
/*!40000 ALTER TABLE `education_qualifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employer_admission_requests`
--

DROP TABLE IF EXISTS `employer_admission_requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employer_admission_requests` (
  `id` int NOT NULL AUTO_INCREMENT,
  `companyName` varchar(100) NOT NULL,
  `contactPerson` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `notes` text,
  `status` enum('pending','approved','rejected') DEFAULT 'pending',
  `verifiedBy` varchar(100) DEFAULT NULL,
  `verifiedAt` timestamp NULL DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employer_admission_requests`
--

LOCK TABLES `employer_admission_requests` WRITE;
/*!40000 ALTER TABLE `employer_admission_requests` DISABLE KEYS */;
/*!40000 ALTER TABLE `employer_admission_requests` ENABLE KEYS */;
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
  `skill_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_posting_skills`
--

LOCK TABLES `job_posting_skills` WRITE;
/*!40000 ALTER TABLE `job_posting_skills` DISABLE KEYS */;
INSERT INTO `job_posting_skills` VALUES (6,7,17),(7,7,18),(11,3,20),(12,2,21),(13,2,22);
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
  `recruiter_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `job_postings_chk_1` CHECK ((`views_count` >= 0)),
  CONSTRAINT `job_postings_chk_2` CHECK ((`applications_count` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_postings`
--

LOCK TABLES `job_postings` WRITE;
/*!40000 ALTER TABLE `job_postings` DISABLE KEYS */;
INSERT INTO `job_postings` VALUES (2,'Digital Marketing Intern','Great opportunity for marketing students to gain hands-on experience in digital marketing campaigns, social media management, and content creation.','Currently enrolled in Marketing/Business program, basic understanding of social media platforms, strong writing skills.','Assist with social media content creation, help analyze campaign metrics, support email marketing efforts, participate in brainstorming sessions.','Remote','internship','entry',20000.00,22000.00,1,'2025-07-03 13:06:29.029023','2025-07-15 16:44:37.354868','2023-11-30',10,0,1),(3,'Digital Marketing Intern','Great opportunity for marketing students to gain hands-on experience in digital marketing campaigns, social media management, and content creation.','Currently enrolled in Marketing/Business program, basic understanding of social media platforms, strong writing skills.','Assist with social media content creation, help analyze campaign metrics, support email marketing efforts, participate in brainstorming sessions.','Remote','internship','entry',20000.00,22000.00,1,'2025-07-03 13:06:32.528599','2025-07-16 07:08:33.795597','2023-11-30',14,0,1),(7,'Travel RN - Emergency Department','13-week contract position for experienced ER nurses at a Level II Trauma Center. Competitive pay and housing stipend available.','Active RN license, BLS/ACLS certification, 2+ years ER experience, ability to start within 2 weeks.','Provide emergency nursing care, collaborate with healthcare team, maintain accurate documentation, follow all hospital protocols.','Chicago,','contract','senior',6500.00,7500.00,1,'2025-07-03 13:21:16.260494','2025-07-15 16:42:47.944504','2023-12-13',11,0,1);
/*!40000 ALTER TABLE `job_postings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_seeker`
--

DROP TABLE IF EXISTS `job_seeker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_seeker` (
  `id` int NOT NULL AUTO_INCREMENT,
  `github_url` varchar(255) DEFAULT NULL,
  `linkedin_url` varchar(255) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `bioData` text,
  `about` text,
  `users_id` int NOT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_job_seeker_users1_idx` (`users_id`),
  CONSTRAINT `fk_job_seeker_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_seeker`
--

LOCK TABLES `job_seeker` WRITE;
/*!40000 ALTER TABLE `job_seeker` DISABLE KEYS */;
INSERT INTO `job_seeker` VALUES (1,'https://github.com/user7','https://linkedin.com/in/user7','Nairobi, Kenya','Backend developer with 3+ years of experience in Node.js, MongoDB, and REST APIs.','I am a backend developer passionate about building scalable and reliable systems. I enjoy working with startups and small businesses to create meaningful software solutions.',7,'2025-05-25 14:05:04','2025-05-25 14:05:04'),(2,'https://linkedin.com/in/user30',' https://linkedin.com/in/user20','Nairobi,Kenya','Backend developer with 3+ years of experience in Node.js, MongoDB, and REST APIs. | I am a backend developer passionate about building scalable and reliable systems. I enjoy working with startups and small businesses to create meaningful software solutions.',NULL,13,'2025-05-28 05:31:51','2025-06-20 14:39:25'),(3,'','','Mombasa,Kenya','Backend developer with 3+ years of experience in Node.js, MongoDB, and REST API','',28,'2025-06-16 13:44:40','2025-06-17 03:47:38'),(4,'','','Arusha,Tanzania','am skilled developer in Laravel in creating minimal and scalable solution to help grow companies ','',29,'2025-06-16 14:03:52','2025-06-16 14:31:53'),(5,'https://linkedin.com/in/user20',' https://linkedin.com/in/user20','Arusha,Tanzania','Fullstack web developer ','',30,'2025-06-16 14:45:24','2025-06-16 14:48:05'),(6,'https://github.com/in/user20',' https://linkedi.com/in/user20','Kisumu,Kenya','a very proactive developer','Am fullstack developer in nodejs c#',31,'2025-06-18 05:03:43','2025-06-18 05:04:37');
/*!40000 ALTER TABLE `job_seeker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobseeker_certification`
--

DROP TABLE IF EXISTS `jobseeker_certification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobseeker_certification` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `issuer` varchar(45) DEFAULT NULL,
  `uploadPath` varchar(500) DEFAULT NULL,
  `awardedDate` date DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_jobSeeker_certification_user` (`userId`),
  CONSTRAINT `fk_jobSeeker_certification_user` FOREIGN KEY (`userId`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobseeker_certification`
--

LOCK TABLES `jobseeker_certification` WRITE;
/*!40000 ALTER TABLE `jobseeker_certification` DISABLE KEYS */;
INSERT INTO `jobseeker_certification` VALUES (2,13,'Amazon Web Services','https://drive.google.com/file/d/1AWS_CERT_ID/preview','2023-08-22','2025-06-04 05:19:28','2025-06-04 05:19:28','AWS Certified Solutions Architect - Associate'),(7,13,'Amazon Web Services','https://drive.google.com/file/d/1AWS_CERT_ID/preview','2023-08-22','2025-06-19 05:18:13','2025-06-19 05:18:13','AWS Certified Solutions Architect - Associate');
/*!40000 ALTER TABLE `jobseeker_certification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruiter`
--

DROP TABLE IF EXISTS `recruiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recruiter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `companyName` varchar(45) NOT NULL,
  `companyLogo` varchar(500) DEFAULT NULL,
  `industry` varchar(250) DEFAULT NULL,
  `contactInfo` varchar(100) DEFAULT NULL,
  `companyEmail` varchar(100) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `users_id` int NOT NULL,
  `isVerified` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `companyEmail_UNIQUE` (`companyEmail`),
  KEY `fk_recruiter_1_idx` (`users_id`),
  CONSTRAINT `fk_recruiter_1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter`
--

LOCK TABLES `recruiter` WRITE;
/*!40000 ALTER TABLE `recruiter` DISABLE KEYS */;
INSERT INTO `recruiter` VALUES (1,'Eujim Solutions',NULL,'software and development','hr@eujimsolution','services@eujm.com','We are a development company who we are committed to proffecient and talented  devs','2025-06-10 20:30:58','2025-07-08 10:24:43',26,NULL);
/*!40000 ALTER TABLE `recruiter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruiter_doc`
--

DROP TABLE IF EXISTS `recruiter_doc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recruiter_doc` (
  `id` int NOT NULL AUTO_INCREMENT,
  `recruiter_id` int NOT NULL,
  `doc_type` varchar(45) DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` enum('approved','pending') DEFAULT 'pending',
  `verifiedAt` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `verifiedBy_id` bigint DEFAULT NULL,
  `upload_path` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_reccruiter_doc_1_idx` (`recruiter_id`),
  KEY `fk_verifiedBy` (`verifiedBy_id`),
  CONSTRAINT `fk_reccruiter_doc_1` FOREIGN KEY (`recruiter_id`) REFERENCES `recruiter` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter_doc`
--

LOCK TABLES `recruiter_doc` WRITE;
/*!40000 ALTER TABLE `recruiter_doc` DISABLE KEYS */;
INSERT INTO `recruiter_doc` VALUES (6,1,'registration certificate','2025-06-18 05:08:55','2025-06-18 05:08:55','pending',NULL,NULL,'recruiter_docs/2025/06/18/webmastercoverletter.pdf');
/*!40000 ALTER TABLE `recruiter_doc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruiter_tracking`
--

DROP TABLE IF EXISTS `recruiter_tracking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recruiter_tracking` (
  `id` int NOT NULL AUTO_INCREMENT,
  `recruiter_id` int NOT NULL,
  `job_seeker_id` int NOT NULL,
  `status` enum('interviewed','shortlisted','hired','rejected','applied','intrested') DEFAULT NULL,
  `notes` text,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `job_posting_id` bigint DEFAULT NULL,
  `user_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_recruiter_tracking_1_idx` (`job_seeker_id`),
  KEY `fk_recruiter_tracking_2_idx` (`recruiter_id`),
  KEY `fk_job_posting` (`job_posting_id`),
  CONSTRAINT `fk_job_posting` FOREIGN KEY (`job_posting_id`) REFERENCES `job_postings` (`id`),
  CONSTRAINT `fk_recruiter_tracking_1` FOREIGN KEY (`job_seeker_id`) REFERENCES `job_seeker` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_recruiter_tracking_2` FOREIGN KEY (`recruiter_id`) REFERENCES `recruiter` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter_tracking`
--

LOCK TABLES `recruiter_tracking` WRITE;
/*!40000 ALTER TABLE `recruiter_tracking` DISABLE KEYS */;
INSERT INTO `recruiter_tracking` VALUES (1,1,2,'rejected',NULL,'2025-06-13 05:13:18','2025-06-15 07:21:54',NULL,'recruiter'),(2,1,2,'shortlisted','some of the skills displayed by the user were not satisfying','2025-06-13 05:14:39','2025-06-18 05:08:19',NULL,'recruiter'),(6,1,2,'interviewed','Interested in MongoDB skills','2025-06-13 12:50:16','2025-06-15 07:31:25',NULL,'recruiter'),(7,1,1,'shortlisted',NULL,'2025-06-17 06:17:33','2025-06-17 06:17:33',NULL,'recruiter'),(8,1,1,'shortlisted',NULL,'2025-07-07 07:49:47','2025-07-07 07:49:47',NULL,'recruiter'),(9,1,2,'shortlisted',NULL,'2025-07-07 10:11:27','2025-07-07 10:11:27',NULL,'recruiter'),(10,1,2,'shortlisted',NULL,'2025-07-07 10:13:27','2025-07-07 10:13:27',NULL,'recruiter'),(12,1,2,'intrested','Candidate has been shortlisted after initial screening.','2025-07-07 10:17:55','2025-07-07 10:17:55',7,'recruiter'),(13,1,2,'intrested','Candidate has been shortlisted after initial screening.','2025-07-08 06:55:12','2025-07-08 06:55:12',7,'recruiter'),(14,1,2,'intrested','Candidate has been shortlisted after initial screening.','2025-07-08 06:55:26','2025-07-08 06:55:26',7,'recruiter'),(15,1,2,'intrested','Candidate has been shortlisted after initial screening.','2025-07-08 06:57:27','2025-07-08 06:57:27',7,'recruiter'),(16,1,2,'intrested','Candidate has been shortlisted after initial screening.','2025-07-08 07:00:34','2025-07-08 07:00:34',7,'recruiter'),(18,1,2,'applied','Candidate has been shortlisted after initial screening.','2025-07-16 05:05:07','2025-07-16 05:05:07',3,'recruiter');
/*!40000 ALTER TABLE `recruiter_tracking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skillSet`
--

DROP TABLE IF EXISTS `skillSet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skillSet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `skill_id` int DEFAULT NULL,
  `proffeciency_level` enum('begginner','intermediate','midlevel','proffessional') DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `userId` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_skillSet_2_idx` (`skill_id`),
  KEY `fk_jobSeeker_skills_user` (`userId`),
  CONSTRAINT `fk_jobSeeker_skills_user` FOREIGN KEY (`userId`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_skillSet_2` FOREIGN KEY (`skill_id`) REFERENCES `skills` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skillSet`
--

LOCK TABLES `skillSet` WRITE;
/*!40000 ALTER TABLE `skillSet` DISABLE KEYS */;
INSERT INTO `skillSet` VALUES (7,1,'proffessional','2025-05-25 14:14:47','2025-05-27 08:39:44',7),(8,2,'midlevel','2025-05-25 14:14:47','2025-05-27 08:39:44',7),(9,3,'intermediate','2025-05-25 14:14:47','2025-05-27 08:39:44',7),(13,10,'begginner','2025-05-29 09:36:39','2025-05-29 09:36:39',5),(14,10,'begginner','2025-05-30 05:25:08','2025-05-30 05:25:08',13),(19,13,'intermediate','2025-06-09 05:59:03','2025-06-09 05:59:03',13),(20,13,'intermediate','2025-06-16 14:10:26','2025-06-16 14:10:26',29),(21,9,'begginner','2025-06-17 03:45:35','2025-06-17 03:45:35',28),(22,15,'begginner','2025-06-18 05:04:57','2025-06-18 05:04:57',31),(24,16,'midlevel','2025-06-18 05:05:20','2025-06-18 05:05:20',31);
/*!40000 ALTER TABLE `skillSet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills`
--

DROP TABLE IF EXISTS `skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `skillName` varchar(45) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
INSERT INTO `skills` VALUES (1,'Node.js','A JavaScript runtime built on Chrome\'s V8 engine for building fast and scalable server-side applications.'),(2,'MongoDB','A NoSQL database known for its flexibility and JSON-like documents.'),(3,'Express.js','A minimal and flexible Node.js web application framework.'),(4,'Docker','A platform for developing, shipping, and running applications in containers.'),(5,'Git','A distributed version control system for tracking changes in source code.'),(6,'PostgreSQL','A powerful, open-source relational database system.'),(7,'Redis','An in-memory key-value store used as a database, cache, and message broker.'),(8,'GraphQL','A query language for APIs and a runtime for executing those queries.'),(9,'TypeScript','A typed superset of JavaScript that compiles to plain JavaScript.'),(10,'REST API','A software architectural style for designing networked applications using stateless communication.'),(11,'react development',''),(12,'Low Level',''),(13,'Web Design',''),(14,'Laravel',''),(15,'Express',''),(16,'Firebase',''),(17,'Python',''),(18,'Javascript',''),(19,'Java',''),(20,'Nodejs',''),(21,'C#',''),(22,'digital marketing','');
/*!40000 ALTER TABLE `skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `isVerified` tinyint DEFAULT NULL,
  `verificationCode` varchar(45) DEFAULT NULL,
  `role` enum('employer','jobseeker','superAdmin','admin') DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_active` tinyint(1) DEFAULT '1',
  `deleted_at` datetime(6) DEFAULT NULL,
  `deleted_by_id` int DEFAULT NULL,
  `deletion_reason` longtext,
  `is_deleted` tinyint(1) NOT NULL,
  `is_pending` tinyint(1) NOT NULL,
  `is_suspended` tinyint(1) NOT NULL,
  `restored_by_id` int DEFAULT NULL,
  `lastName` varchar(150) NOT NULL,
  `isStaff` tinyint(1) DEFAULT '0',
  `isSuperuser` tinyint(1) DEFAULT '0',
  `lastLogin` datetime DEFAULT NULL,
  `dateJoined` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `users_deleted_by_id_d342c553_fk_users_id` (`deleted_by_id`),
  KEY `users_restored_by_id_502fb5c0_fk_users_id` (`restored_by_id`),
  CONSTRAINT `users_deleted_by_id_d342c553_fk_users_id` FOREIGN KEY (`deleted_by_id`) REFERENCES `users` (`id`),
  CONSTRAINT `users_restored_by_id_502fb5c0_fk_users_id` FOREIGN KEY (`restored_by_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'Ancellotti','natahaniel23@gmail.com','pbkdf2_sha256$600000$6yauDLNsryDOk8SKmJi139$tM3wSrrHpKR3xEFkmI4aM6ji98iE6a4OfYZznUNwyDQ=',1,'f9f8cb6ad7804ba5918e5a7d529c7891',NULL,'2025-05-15 13:59:12','2025-05-25 08:03:59',0,'2025-05-25 11:03:58.894956',5,NULL,1,1,0,NULL,'',0,0,NULL,NULL),(3,'Ancellotti','kimotho@gmail.com','pbkdf2_sha256$600000$XOP5RAEInQ9O9B1Zvjh0Jh$56YIHPdzosyjBzB35lImJlCeMudhx520GYKc8susa1w=',0,'7601bed3f1f64e8cb22efd77d735094c',NULL,'2025-05-15 14:08:12','2025-06-10 04:42:47',1,NULL,NULL,NULL,0,1,0,NULL,'',0,0,NULL,NULL),(4,'Ancellotti','kimot34ho@gmail.com','pbkdf2_sha256$600000$pcheaVHjSQ9nDwSWeCrrQg$/37bccexjU077ez5YmzmNWMiYpFnDn83llGHe/Hq6XI=',1,'5c1b5d2995b646c8ab2bf3bbae95a00c',NULL,'2025-05-15 14:14:15','2025-06-10 04:42:57',1,NULL,NULL,NULL,0,1,0,NULL,'',0,0,NULL,NULL),(5,'TImothy','kimilu@gmail.com','pbkdf2_sha256$600000$y49hGSp4QewDHGbKJ4Id6q$R5LGiGS1T7T91ax9niKB5CQwOKM9Dsp13hbZnW7DejI=',1,'b45ade46fe2a4bb09e89d31099c0df35','superAdmin','2025-05-19 05:37:49','2025-06-22 12:09:36',1,NULL,NULL,NULL,0,1,0,NULL,'',0,0,NULL,NULL),(6,'Ancelloti','ancelloti@gmail.com','pbkdf2_sha256$600000$zjbCdjxz7VCJ5rBtoWfysl$cRJnHnOzfAWZpZPEkktv5f9S0UvUGG0WA4Xytgdf3Lg=',1,'2df2933fba6640a4b8c9bb28e904cb98','jobseeker','2025-05-19 17:11:07','2025-05-25 07:47:24',1,NULL,NULL,NULL,0,1,0,NULL,'',0,0,NULL,NULL),(7,'Ancelloti','kariuki@gmail.com','pbkdf2_sha256$600000$oYBQWODjwCon7nSYDWGCxu$EqmN1tS2TgISqwfSdPNAb5d4wUgTcR4BcM0lxbuHucw=',1,'4f71c27f3b9e41d98353a2f6f6b97e69','jobseeker','2025-05-19 17:13:27','2025-05-25 07:52:29',1,'2025-05-21 13:00:58.476333',5,NULL,0,1,0,NULL,'',0,0,NULL,NULL),(8,'Ancelloti','muchoki@gmail.com','pbkdf2_sha256$600000$SypS9t9KknF4exUcJPHSl3$V6OA+4tVyv6zR7ROWsxpsrVZRuVNn+Z6/GTXM1WE3ic=',1,'80d028a87a09464c925860f14a648583','employer','2025-05-22 07:17:51','2025-05-25 07:41:26',0,'2025-05-25 10:41:25.572640',5,NULL,1,1,1,NULL,'',0,0,NULL,NULL),(9,'Claive','muchoki145@gmail.com','pbkdf2_sha256$600000$lRw72gRuyUdg9s5ycPZiMQ$q5jCxy1ufbFclEaeJYSw+/umUs8hBfYcUrrLoz4/SBE=',1,'aeab2dbd79804fe08953db0f466b0c37','employer','2025-05-23 04:39:20','2025-05-25 07:42:00',0,'2025-05-25 10:42:00.417123',5,NULL,1,0,0,NULL,'',0,0,NULL,NULL),(10,'Ancelloti','muchoki34@gmail.com','pbkdf2_sha256$600000$08NRaWyFPzSVDaqTmURiAY$2/9msfNQKOPXX8s9GywFZDyansp5uBCW9mZHCTnnXVg=',1,'28dc5cd2e8804eddaa0b8b57236f3d10','employer','2025-05-23 08:22:40','2025-05-25 08:04:45',1,NULL,NULL,NULL,0,1,0,NULL,'',0,0,NULL,NULL),(11,'Faith','museo@gmail.com','pbkdf2_sha256$600000$PnxhpqtMAOYEljFjmDD9zM$LMfLV4kk4DSoq35Ol7rsD+jIZrnqBi+lV0Um2r4FfYU=',1,'99b1de8b6db243ce9648af8334dd6b6f','employer','2025-05-25 09:32:08','2025-05-25 09:32:49',1,NULL,NULL,NULL,0,1,0,NULL,'',0,0,NULL,NULL),(12,'Kinoti','kinoti@gmail.com','pbkdf2_sha256$600000$JFPlQAkr4y5WsF5QZXsBU1$eUV+IK4BhbZjQud2qQpupV9tz/Zg+CqHbA6/s7yKT4o=',1,'22a2ce31c96243008655dbf3922b3342','jobseeker','2025-05-25 09:53:08','2025-05-25 10:06:47',1,NULL,NULL,NULL,0,1,0,NULL,'',0,0,NULL,NULL),(13,'Princes Antony','mbugua@gmail.com','pbkdf2_sha256$600000$QrtYjrMVh8oXHv1rFjg8Wa$+5VeKNObS4x82lWqCsa92bbLWaWDnLc26/LI0SJsPnE=',1,'bd32e50685484f738e9589522e9f3da2','jobseeker','2025-05-28 04:36:55','2025-06-22 07:11:43',1,NULL,NULL,NULL,0,0,0,NULL,'',0,0,NULL,NULL),(15,'Mary','maryodhiambo260@gmail.com','pbkdf2_sha256$870000$HHukLNqc0wXwQsjA8KtBQ4$I53LZQbESFzdjNIE+qL8f9eXkf1nE31JamJJP2I2CRU=',1,NULL,'jobseeker','2025-06-09 07:06:45','2025-06-10 18:30:55',1,NULL,NULL,NULL,0,1,0,NULL,'Maria',0,0,NULL,NULL),(16,'Mary','maryodhiambo261@gmail.com','pbkdf2_sha256$870000$qVMoZkoqHtPMgbr7yj4Fp3$9V/RWphYa4eHvUJIc0mFOodV+YR8itRAja0xggTLBNc=',1,NULL,'jobseeker','2025-06-09 09:34:32','2025-06-10 18:32:39',1,NULL,NULL,NULL,0,1,0,NULL,'Maria',0,0,NULL,NULL),(17,'Mary','maryodhiambo262@gmail.com','pbkdf2_sha256$870000$m4y8JmH1ap4KDMiCce9qRP$9LZi0OtKrJvA4j6EqIysdSillLkgBl9xiWB/ra+5evo=',1,NULL,'jobseeker','2025-06-09 09:38:02','2025-06-10 18:33:05',1,NULL,NULL,NULL,0,1,0,NULL,'Maria',0,0,NULL,NULL),(18,'Mary','maryodhiambo264@gmail.com','pbkdf2_sha256$870000$4rc7jCXaVogqhvV2vbs3sq$WkkHZ5d1iFslaMLhicRlJrtCuhNa6ji+J/F5ru61q7k=',0,'99b644ef-7049-4284-a83a-a449cbdf4d60','jobseeker','2025-06-09 09:46:58','2025-06-09 09:46:58',1,NULL,NULL,NULL,0,1,0,NULL,'Maria',0,0,NULL,NULL),(19,'Mary','maryodhiambo265@gmail.com','pbkdf2_sha256$870000$8pwr9xxJJEJMrbIWcrMiwF$FgiR9uRdXDfHTByjYlukm5uxXuEYx8l+MplFMFLOCig=',0,'8b8b343c-e673-4f38-b5e1-618b3ef07509','jobseeker','2025-06-09 09:54:32','2025-06-09 09:54:32',1,NULL,NULL,NULL,0,1,0,NULL,'Maria',0,0,NULL,NULL),(20,'Mary','maryodhiambo266@gmail.com','pbkdf2_sha256$870000$tsuabnwJiYwpfrM4FIkLHM$UL/G1WmG5wsUas/t1i8bs9PInN2JvgF0l/7lUCvzsoM=',0,'00e55047-346a-4c43-86ad-29cb827f328f','jobseeker','2025-06-09 09:56:35','2025-06-09 09:56:35',1,NULL,NULL,NULL,0,1,0,NULL,'Maria',0,0,NULL,NULL),(21,'Mary','maryodhiambo267@gmail.com','pbkdf2_sha256$870000$yO0CuqHGi4s2nlpbAcflEu$OI0QlAl0mi5QYC1cNlM7FVkUnXemrw17h/Te9is3lO4=',0,'e6e860a5-992d-4703-8e4c-36ad3f79e0ff','jobseeker','2025-06-09 10:04:17','2025-06-09 10:04:17',1,NULL,NULL,NULL,0,1,0,NULL,'Maria',0,0,NULL,NULL),(22,'Mary','maryodhiambo268@gmail.com','pbkdf2_sha256$870000$HqcboboDHNKnU6MSrjNqRv$6dut9fxeI8LkcLPHBtNywW5jBwALd0cj0OcgmEcGtTs=',0,'92ebf1b1-3c47-4566-907b-703648798a36','jobseeker','2025-06-09 10:05:39','2025-06-09 10:05:39',1,NULL,NULL,NULL,0,1,0,NULL,'Maria',0,0,NULL,NULL),(23,'Mary','maryodhiambo269@gmail.com','pbkdf2_sha256$870000$UgJfBFBVOwoiyAWWx1lHNj$iRVxNx7Z32iksKiBiJyYt9yIvzf8BFeMh8G4s3c8DXY=',0,'137924ed-5073-4def-b277-096977466992','jobseeker','2025-06-09 10:17:44','2025-06-09 10:17:44',1,NULL,NULL,NULL,0,1,0,NULL,'Maria',0,0,NULL,NULL),(24,'Pompeo','popmpeo@gmail.com','pbkdf2_sha256$600000$Cs8hVvexd3GQX7FNZcmStH$GREXJj+TKRLFs6P0iBo2heJlMJ/24nESI0Y+bOSgJG0=',0,'67efb7a5f07a4893a647b63918642d25','jobseeker','2025-06-10 06:00:21','2025-06-10 06:00:21',1,NULL,NULL,NULL,0,1,0,NULL,'Maria',0,0,NULL,NULL),(25,'Wera','wera@gmail.com','pbkdf2_sha256$600000$HKrCoCFz55L0azH6xLSa3K$0ag3vrr4MzODd3obM5Nd+xdK3JKdqv03dA8cjlC/gvg=',1,'dd1f721299bd430f87cebecee7d95d6a','employer','2025-06-10 06:03:31','2025-06-10 06:03:53',1,NULL,NULL,NULL,0,1,0,NULL,'Kinoti',0,0,NULL,NULL),(26,'Timon','alois@gmail.com','pbkdf2_sha256$600000$daPYMOLrhdTzMoK5ybtgBX$a98CY8a67vIuQh9SsozNlORVniolt6v85HyL2Vjlhrk=',1,'e7ec3f3d1ede48238318931ff5e3f1e8','employer','2025-06-10 06:33:11','2025-06-18 05:01:14',1,NULL,NULL,NULL,0,1,0,NULL,'ALOIS',0,0,NULL,NULL),(27,'Timor','atieno@gmail.com','pbkdf2_sha256$600000$rsQqGyR576IzN24jCYgmyw$yfBz4G7EVmCjePMVgbgVfT6fEDbOZcV++qkIpmP4sEY=',1,'badf23c1c7bc4dcc94bd4570f6ad0ada','employer','2025-06-10 06:35:55','2025-06-10 17:33:08',1,NULL,NULL,NULL,0,1,0,NULL,'Fetch',0,0,NULL,NULL),(28,'Kimemia','kimemia@gmail.com','pbkdf2_sha256$600000$y8J0N1s2998UaOfTXm99eg$CpXNLn+h+MrGIpgszAkDlhU5MD+e3WhEjsOBZpG2XTU=',1,'dca5f6b94500481689f60c2c038155c6','jobseeker','2025-06-16 09:46:53','2025-06-16 09:50:10',1,NULL,NULL,NULL,0,1,0,NULL,'Mwendwa',0,0,NULL,NULL),(29,'Alfredd','albert@gmail.com','pbkdf2_sha256$600000$2mCibhRnu2l6JEStoVBHHJ$zvXehljXbT7jzpAYHDbcSmXVH0bAFs0b3WL8CdlLAEI=',1,'055beddae6fe4b379bcb97d0ac528f07','jobseeker','2025-06-16 13:54:12','2025-06-16 13:55:49',1,NULL,NULL,NULL,0,1,0,NULL,'Albert',0,0,NULL,NULL),(30,'Felix','alex@gmail.com','pbkdf2_sha256$600000$2fvMciqO4uPgYnoC2q3ZyC$b6huwZ68+3cOup7E9w81OxbgxkyJcBC9VB48F1SljvI=',1,'3a16144c57934c448163c96c710f33cc','jobseeker','2025-06-16 14:34:17','2025-06-16 14:34:46',1,NULL,NULL,NULL,0,1,0,NULL,'Alex',0,0,NULL,NULL),(31,'Gloria','mutheu@gmail.com','pbkdf2_sha256$600000$41vXnd3Wvsq2Hnk2ETYtqj$RhQVjLC8wmmQR5iq5uL7/vT6J2b35B5hnSquZn7ToGE=',1,'6b841b798c324f05b345d3d26d4621c6','jobseeker','2025-06-18 04:58:02','2025-06-18 04:58:57',1,NULL,NULL,NULL,0,1,0,NULL,'Mutheu',0,0,NULL,NULL),(32,'Wera','employer@gmail.com','pbkdf2_sha256$600000$BmuinjVC0afwhPjAc73DZC$jThnM0YL0+sneM3al/qWTlAuM5UefhlLnCwHSNLkFpA=',1,'681f7dca1aca434097cedb6ca5ac7f30','employer','2025-06-19 05:36:31','2025-06-19 06:37:47',1,NULL,NULL,NULL,0,1,0,NULL,'Kinoti',0,0,NULL,NULL),(33,'Wera','kinotiwera@gmail.com','pbkdf2_sha256$600000$63HbrfpWV6xE5BOwd723Y0$5s3mcXqL7wPzt/Pq9kHwHjbNIIGLhZLifFQjy49faUc=',1,'6e8109e164b0466a8587bc1505fe4cf0','employer','2025-06-19 06:57:34','2025-06-19 07:05:02',1,NULL,NULL,NULL,0,1,0,NULL,'Kinoti',0,0,NULL,NULL),(34,'Wera','babarian@gmail.com','pbkdf2_sha256$600000$y6zH8LJTJQyLnozckho7dE$YDFnnIHh5xHl4Ew8qKF6F5ApiGV1qJZpAPK7BWLZrJk=',1,'ef46e47c2f0c44f29d346d90f22b9120','employer','2025-06-19 07:10:34','2025-06-19 07:18:09',1,NULL,NULL,NULL,0,1,0,NULL,'Kinoti',0,0,NULL,NULL),(35,'Wera','martin@gmail.com','pbkdf2_sha256$600000$3MyH61eBSUw2BqLoS6hD4y$19ysDciG0J8VzxF4n9ToIgcfNKHQcGGOup4Ly9AtscE=',0,'4e25c8165bcb4a2dbbbbcb746974bdce','employer','2025-06-26 13:58:00','2025-06-26 13:58:00',1,NULL,NULL,NULL,0,1,0,NULL,'Kinoti',0,0,NULL,'2025-06-26 16:58:00');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-16 14:39:44
