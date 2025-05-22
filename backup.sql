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
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add job seeker',8,'add_jobseeker'),(30,'Can change job seeker',8,'change_jobseeker'),(31,'Can delete job seeker',8,'delete_jobseeker'),(32,'Can view job seeker',8,'view_jobseeker'),(33,'Can add job seeker certification',9,'add_jobseekercertification'),(34,'Can change job seeker certification',9,'change_jobseekercertification'),(35,'Can delete job seeker certification',9,'delete_jobseekercertification'),(36,'Can view job seeker certification',9,'view_jobseekercertification'),(37,'Can add skill',10,'add_skill'),(38,'Can change skill',10,'change_skill'),(39,'Can delete skill',10,'delete_skill'),(40,'Can view skill',10,'view_skill'),(41,'Can add skill set',11,'add_skillset'),(42,'Can change skill set',11,'change_skillset'),(43,'Can delete skill set',11,'delete_skillset'),(44,'Can view skill set',11,'view_skillset'),(45,'Can add recruiter',12,'add_recruiter'),(46,'Can change recruiter',12,'change_recruiter'),(47,'Can delete recruiter',12,'delete_recruiter'),(48,'Can view recruiter',12,'view_recruiter'),(49,'Can add recruiter doc',13,'add_recruiterdoc'),(50,'Can change recruiter doc',13,'change_recruiterdoc'),(51,'Can delete recruiter doc',13,'delete_recruiterdoc'),(52,'Can view recruiter doc',13,'view_recruiterdoc'),(53,'Can add recruiter tracking',14,'add_recruitertracking'),(54,'Can change recruiter tracking',14,'change_recruitertracking'),(55,'Can delete recruiter tracking',14,'delete_recruitertracking'),(56,'Can view recruiter tracking',14,'view_recruitertracking');
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'jobseeker','jobseeker'),(9,'jobseeker','jobseekercertification'),(12,'recruiter','recruiter'),(13,'recruiter','recruiterdoc'),(14,'recruiter','recruitertracking'),(6,'sessions','session'),(10,'skills','skill'),(11,'skills','skillset'),(7,'users','user');
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
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-05-15 09:22:11.878299'),(2,'auth','0001_initial','2025-05-15 09:23:53.948290'),(3,'admin','0001_initial','2025-05-15 09:24:07.564897'),(4,'admin','0002_logentry_remove_auto_add','2025-05-15 09:24:07.796385'),(5,'admin','0003_logentry_add_action_flag_choices','2025-05-15 09:24:08.205006'),(6,'contenttypes','0002_remove_content_type_name','2025-05-15 09:24:17.924144'),(7,'auth','0002_alter_permission_name_max_length','2025-05-15 09:24:22.971538'),(8,'auth','0003_alter_user_email_max_length','2025-05-15 09:24:28.175217'),(9,'auth','0004_alter_user_username_opts','2025-05-15 09:24:28.635598'),(10,'auth','0005_alter_user_last_login_null','2025-05-15 09:24:32.806316'),(11,'auth','0006_require_contenttypes_0002','2025-05-15 09:24:32.962118'),(12,'auth','0007_alter_validators_add_error_messages','2025-05-15 09:24:33.352931'),(13,'auth','0008_alter_user_username_max_length','2025-05-15 09:24:39.889459'),(14,'auth','0009_alter_user_last_name_max_length','2025-05-15 09:24:45.499261'),(15,'auth','0010_alter_group_name_max_length','2025-05-15 09:24:55.213161'),(16,'auth','0011_update_proxy_permissions','2025-05-15 09:24:55.840145'),(17,'auth','0012_alter_user_first_name_max_length','2025-05-15 09:25:06.836508'),(18,'sessions','0001_initial','2025-05-15 09:25:14.080691'),(19,'jobseeker','0001_initial','2025-05-19 11:29:34.446181'),(20,'recruiter','0001_initial','2025-05-19 11:29:36.284047'),(21,'skills','0001_initial','2025-05-19 11:29:36.578781'),(22,'users','0001_initial','2025-05-19 11:29:36.954171'),(23,'users','0002_alter_user_options','2025-05-19 11:32:36.716450'),(24,'users','0003_alter_user_options','2025-05-19 11:47:01.362144'),(25,'users','0004_alter_user_options','2025-05-21 07:18:13.111064'),(26,'users','0005_user_deleted_at_user_deleted_by_user_deletion_reason_and_more','2025-05-21 10:42:26.331982');
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
-- Table structure for table `job_seeker`
--

DROP TABLE IF EXISTS `job_seeker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_seeker` (
  `id` int NOT NULL AUTO_INCREMENT,
  `github_url` varchar(255) DEFAULT NULL,
  `linkedin_url` varchar(255) DEFAULT NULL,
  `InstitutionName` varchar(45) DEFAULT NULL,
  `year_of_joining` date DEFAULT NULL,
  `year_of_completion` date DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_seeker`
--

LOCK TABLES `job_seeker` WRITE;
/*!40000 ALTER TABLE `job_seeker` DISABLE KEYS */;
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
  `job_seeker_id` int NOT NULL,
  `issuer` varchar(45) DEFAULT NULL,
  `uploadPath` varchar(500) DEFAULT NULL,
  `awardedDate` date DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_jobseeker_certification_1_idx` (`job_seeker_id`),
  CONSTRAINT `fk_jobseeker_certification_1` FOREIGN KEY (`job_seeker_id`) REFERENCES `job_seeker` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobseeker_certification`
--

LOCK TABLES `jobseeker_certification` WRITE;
/*!40000 ALTER TABLE `jobseeker_certification` DISABLE KEYS */;
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
  `industry` varchar(45) DEFAULT NULL,
  `contactInfo` varchar(45) DEFAULT NULL,
  `companyEmail` varchar(45) NOT NULL,
  `description` varchar(45) DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `users_id` int NOT NULL,
  `isVerified` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `companyEmail_UNIQUE` (`companyEmail`),
  KEY `fk_recruiter_1_idx` (`users_id`),
  CONSTRAINT `fk_recruiter_1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter`
--

LOCK TABLES `recruiter` WRITE;
/*!40000 ALTER TABLE `recruiter` DISABLE KEYS */;
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
  `uploadPath` varchar(500) DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` enum('approved','pending') DEFAULT 'pending',
  `verifiedBy` varchar(100) DEFAULT NULL,
  `verifiedAt` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_reccruiter_doc_1_idx` (`recruiter_id`),
  CONSTRAINT `fk_reccruiter_doc_1` FOREIGN KEY (`recruiter_id`) REFERENCES `recruiter` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter_doc`
--

LOCK TABLES `recruiter_doc` WRITE;
/*!40000 ALTER TABLE `recruiter_doc` DISABLE KEYS */;
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
  `status` enum('interviewed','shortlisted','hired','rejected') DEFAULT 'shortlisted',
  `notes` text,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_recruiter_tracking_1_idx` (`job_seeker_id`),
  KEY `fk_recruiter_tracking_2_idx` (`recruiter_id`),
  CONSTRAINT `fk_recruiter_tracking_1` FOREIGN KEY (`job_seeker_id`) REFERENCES `job_seeker` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_recruiter_tracking_2` FOREIGN KEY (`recruiter_id`) REFERENCES `recruiter` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter_tracking`
--

LOCK TABLES `recruiter_tracking` WRITE;
/*!40000 ALTER TABLE `recruiter_tracking` DISABLE KEYS */;
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
  `job_seeker_id` int DEFAULT NULL,
  `skill_id` int DEFAULT NULL,
  `proffeciency_level` enum('begginner','intermediate','midlevel','proffessional') DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_skillSet_1_idx` (`job_seeker_id`),
  KEY `fk_skillSet_2_idx` (`skill_id`),
  CONSTRAINT `fk_skillSet_1` FOREIGN KEY (`job_seeker_id`) REFERENCES `job_seeker` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_skillSet_2` FOREIGN KEY (`skill_id`) REFERENCES `skills` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skillSet`
--

LOCK TABLES `skillSet` WRITE;
/*!40000 ALTER TABLE `skillSet` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
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
  `secondName` varchar(45) NOT NULL,
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `users_deleted_by_id_d342c553_fk_users_id` (`deleted_by_id`),
  KEY `users_restored_by_id_502fb5c0_fk_users_id` (`restored_by_id`),
  CONSTRAINT `users_deleted_by_id_d342c553_fk_users_id` FOREIGN KEY (`deleted_by_id`) REFERENCES `users` (`id`),
  CONSTRAINT `users_restored_by_id_502fb5c0_fk_users_id` FOREIGN KEY (`restored_by_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'Ancellotti','Nathaniel','natahaniel23@gmail.com','pbkdf2_sha256$600000$6yauDLNsryDOk8SKmJi139$tM3wSrrHpKR3xEFkmI4aM6ji98iE6a4OfYZznUNwyDQ=',0,'f9f8cb6ad7804ba5918e5a7d529c7891',NULL,'2025-05-15 13:59:12','2025-05-15 13:59:12',1,NULL,NULL,NULL,0,1,1,NULL),(3,'Ancellotti','Nathaniel','kimotho@gmail.com','pbkdf2_sha256$600000$XOP5RAEInQ9O9B1Zvjh0Jh$56YIHPdzosyjBzB35lImJlCeMudhx520GYKc8susa1w=',0,'7601bed3f1f64e8cb22efd77d735094c',NULL,'2025-05-15 14:08:12','2025-05-15 14:08:12',1,NULL,NULL,NULL,0,1,1,NULL),(4,'Ancellotti','Nathaniel','kimot34ho@gmail.com','pbkdf2_sha256$600000$pcheaVHjSQ9nDwSWeCrrQg$/37bccexjU077ez5YmzmNWMiYpFnDn83llGHe/Hq6XI=',0,'5c1b5d2995b646c8ab2bf3bbae95a00c',NULL,'2025-05-15 14:14:15','2025-05-15 14:14:15',1,NULL,NULL,NULL,0,1,1,NULL),(5,'TImothy','Kimilu','kimilu@gmail.com','pbkdf2_sha256$600000$d9JvxtKNOWO1PAQr1aec03$SKNcv0sywIbDnGgfIlb9894GEgIuK4KmdAex/WdheBk=',1,'b45ade46fe2a4bb09e89d31099c0df35','superAdmin','2025-05-19 05:37:49','2025-05-19 05:58:36',1,NULL,NULL,NULL,0,1,1,NULL),(6,'Ancelloti','Kimilu','ancelloti@gmail.com','pbkdf2_sha256$600000$zjbCdjxz7VCJ5rBtoWfysl$cRJnHnOzfAWZpZPEkktv5f9S0UvUGG0WA4Xytgdf3Lg=',1,'2df2933fba6640a4b8c9bb28e904cb98','jobseeker','2025-05-19 17:11:07','2025-05-19 17:12:44',1,NULL,NULL,NULL,0,1,1,NULL),(7,'Ancelloti','Kariuki','kariuki@gmail.com','pbkdf2_sha256$600000$oYBQWODjwCon7nSYDWGCxu$EqmN1tS2TgISqwfSdPNAb5d4wUgTcR4BcM0lxbuHucw=',0,'4f71c27f3b9e41d98353a2f6f6b97e69','jobseeker','2025-05-19 17:13:27','2025-05-21 10:35:28',1,'2025-05-21 13:00:58.476333',5,NULL,0,1,1,NULL);
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

-- Dump completed on 2025-05-22  9:50:50
