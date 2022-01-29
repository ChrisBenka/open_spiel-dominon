# Copyright 2019 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as python3
"""Tests for Python Dominion."""

from absl.testing import absltest
from open_spiel.python.games import dominion


class DominionTest(absltest.TestCase):
    DEFAULT_PARAMS = {"num_players": 2}

    def test_can_create_and_state(self):
        game = dominion.DominionGame(DominionTest.DEFAULT_PARAMS)
        state = game.new_initial_state()
        self.assertIsNotNone(state)

    def test_state_rep_returns_supply_draw_discard_trash_piles_and_hands(self):
        game = dominion.DominionGame(DominionTest.DEFAULT_PARAMS)
        state = game.new_initial_state()
        self.assertIsNotNone(state.draw_piles)
        self.assertIsNotNone(state.discard_piles)
        self.assertIsNotNone(state.hands)
        self.assertIsNotNone(state.trash_piles)
        self.assertIsNotNone(state.victory_points)

    def test_each_player_starts_with_7coppers_3_estates_in_draw_piles(self):
        game = dominion.DominionGame(DominionTest.DEFAULT_PARAMS)
        state = game.new_initial_state()
        self.assertEqual(len(state.draw_piles), DominionTest.DEFAULT_PARAMS["num_players"])
        self.assertEqual(len(state.victory_points), DominionTest.DEFAULT_PARAMS["num_players"])
        self.assertEqual(len(state.hands), DominionTest.DEFAULT_PARAMS["num_players"])
        for initial_draw_pile in state.draw_piles :
            self.assertEqual(len(list(filter(lambda card: card.name == 'Copper',initial_draw_pile))),7)
            self.assertEqual(len(list(filter(lambda card: card.name == 'Estate',initial_draw_pile))),3)

if __name__ == "__main__":
    absltest.main()
