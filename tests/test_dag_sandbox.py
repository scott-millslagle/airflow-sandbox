import unittest
from airflow.models import DagBag

class TestMyDAG(unittest.TestCase):
    def setUp(self):
        self.dagbag = DagBag(dag_folder="dags/", include_examples=False)

    def test_dag_loaded(self):
        dag = self.dagbag.get_dag("my_dag")
        self.assertIsNotNone(dag)
        self.assertEqual(len(dag.tasks), 3)

    def test_task_dependencies(self):
        dag = self.dagbag.get_dag("my_dag")
        start_task = dag.get_task("start_task")
        hello_task = dag.get_task("hello_task")
        end_task = dag.get_task("end_task")

        start_task_downstream = {t.task_id for t in start_task.downstream_list}
        self.assertSetEqual(start_task_downstream, {"hello_task"})

        hello_task_upstream = {t.task_id for t in hello_task.upstream_list}
        hello_task_downstream = {t.task_id for t in hello_task.downstream_list}
        self.assertSetEqual(hello_task_upstream, {"start_task"})
        self.assertSetEqual(hello_task_downstream, {"end_task"})

        end_task_upstream = {t.task_id for t in end_task.upstream_list}
        self.assertSetEqual(end_task_upstream, {"hello_task"})

if __name__ == "__main__":
    unittest.main()