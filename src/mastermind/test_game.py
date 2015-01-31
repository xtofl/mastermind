from mockito.mocking import mock
from mockito.mockito import verify, when
from mastermind.game import MasterMind

__author__ = 'xtofl'

from unittest import TestCase


class TestMasterMind(TestCase):

    def test_random_seed_is_used_to_create_secret(self):
        random = mock()
        when(random).called().thenReturn(1).thenReturn(2).thenReturn(4).thenReturn(5)
        game = MasterMind(random=random.called)
        game.start()
        verify(random, times=4).called()
        self.assertEqual((4, 0), game.guess([1, 2, 4, 5]))

    def test_response(self):
        random = mock()
        when(random).called().thenReturn(1).thenReturn(2).thenReturn(4).thenReturn(5)
        game = MasterMind(random=random.called)
        game.start()
        self.assertEqual((1, 0), game.guess([1, 6, 7, 8]))
        self.assertEqual((2, 0), game.guess([1, 6, 7, 5]))
        self.assertEqual((1, 1), game.guess([1, 5, 6, 7]))
        self.assertEqual((0, 4), game.guess([5, 4, 1, 2]))
